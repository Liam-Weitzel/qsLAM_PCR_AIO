import sys
from enum import Enum, auto

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class StepState(Enum):
    INACTIVE = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()


class CustomProgressBar(QWidget):
    stepsChanged = Signal(list)
    stateChanged = Signal(int, StepState)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._labels: list[str] = []
        self._states: list[StepState] = []
        self._step_rects: list[QRect] = []

        # animated width of the blue fill
        self._fill_width = 0.0
        self._anim = QPropertyAnimation(self, b"fill_width", self)
        self._anim.setDuration(400)
        self._anim.setEasingCurve(QEasingCurve.InOutQuad)

    # ---------------- property for animation ----------------
    def get_fill_width(self):
        return self._fill_width

    def set_fill_width(self, val):
        self._fill_width = val
        self.update()

    fill_width = Property(float, fget=get_fill_width, fset=set_fill_width)

    # ---------------- API ----------------
    def set_labels(self, labels: list[str]):
        self._labels = labels[:]
        self._states = [StepState.INACTIVE] * len(labels)
        self.stepsChanged.emit(self._labels)
        self.update()

    def get_labels(self):
        return self._labels

    labels = Property(list, fget=get_labels, fset=set_labels, notify=stepsChanged)

    def set_step_state(self, index: int, state: StepState):
        if 0 <= index < len(self._states):
            self._states[index] = state
            self.stateChanged.emit(index, state)
            self._update_animation()
            self.update()

    def get_step_state(self, index: int) -> StepState:
        if 0 <= index < len(self._states):
            return self._states[index]
        return StepState.INACTIVE

    def last_completed_index(self) -> int:
        """
        Returns the index of the last consecutively completed step starting
        from the beginning. Returns -1 if none are completed.
        """
        idx = -1
        for i, st in enumerate(self._states):
            if st == StepState.COMPLETED:
                idx = i
            else:
                break
        return idx

    # ---------------- internal helpers ----------------
    def _update_animation(self):
        if not self._labels:
            return
        number_of_steps = len(self._labels)
        step_width = (self.width() - 20) / number_of_steps  # track width - margins

        # count consecutive completed
        completed_count = 0
        for st in self._states:
            if st == StepState.COMPLETED:
                completed_count += 1
            else:
                break

        if completed_count == 0:
            target_width = 0.0
        elif completed_count >= number_of_steps:
            target_width = self.width() - 20
        else:
            target_width = (completed_count - 0.5) * step_width

        self._anim.stop()
        self._anim.setStartValue(self._fill_width)
        self._anim.setEndValue(target_width)
        self._anim.start()

    # ---------------- Painting ----------------
    def paintEvent(self, event):
        grey = QColor("#777")
        grey2 = QColor("#dfe3e4")
        blue = QColor("#2183dd")
        green = QColor("#009900")
        red = QColor("red")
        white = QColor("#fff")

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.fillRect(self.rect(), white)

        if not self._labels:
            return

        height = 5
        offset = 10
        busy_rect = QRect(0, 0, self.width(), height)
        busy_rect.adjust(offset, 0, -offset, 0)
        busy_rect.moveCenter(self.rect().center())
        painter.fillRect(busy_rect, grey2)

        # blue fill (animated)
        if self._fill_width > 0:
            r_busy = QRect(busy_rect.left(), busy_rect.top(), int(self._fill_width), height)
            painter.fillRect(r_busy, blue)

        number_of_steps = len(self._labels)
        step_width = busy_rect.width() / number_of_steps
        x = busy_rect.left() + step_width / 2
        y = busy_rect.center().y()
        radius = 13

        font_text = painter.font()
        fm = QFontMetrics(font_text)
        r = QRect(0, 0, int(1.5 * radius), int(1.5 * radius))

        self._step_rects.clear()

        for i, (text, state) in enumerate(zip(self._labels, self._states), 0):
            r.moveCenter(QPoint(int(x), int(y)))
            self._step_rects.append(QRect(r))

            if state == StepState.COMPLETED:
                pen = QPen(green, 3)
                painter.setPen(pen)
                painter.setBrush(green)
                painter.drawEllipse(r)
                painter.setPen(white)
                painter.drawText(r, Qt.AlignCenter, "✔")

            elif state == StepState.RUNNING:
                # circle
                pen = QPen(blue, 3)
                painter.setPen(pen)
                painter.setBrush(white)
                painter.drawEllipse(r)

                # triangle ▶
                tri = QPolygon([
                    QPoint(r.center().x() - 3, r.center().y() - 5),
                    QPoint(r.center().x() - 3, r.center().y() + 5),
                    QPoint(r.center().x() + 6, r.center().y()),
                ]) 
                painter.setBrush(blue)
                painter.setPen(Qt.NoPen)
                painter.drawPolygon(tri)

            elif state == StepState.FAILED:
                pen = QPen(red, 3)
                painter.setPen(pen)
                painter.setBrush(red)
                painter.drawEllipse(r)
                painter.setPen(white)
                painter.drawText(r, Qt.AlignCenter, "✗")

            else:  # INACTIVE
                pen = QPen(grey2, 3)
                painter.setPen(pen)
                painter.setBrush(white)
                painter.drawEllipse(r)

            # label text
            rect = fm.boundingRect(text)
            rect.moveCenter(QPoint(int(x), int(y + 2 * radius)))
            if state == StepState.RUNNING:
                painter.setPen(blue)
            else:
                painter.setPen(QColor("black"))
            painter.setFont(font_text)
            painter.drawText(rect, Qt.AlignCenter, text)

            x += step_width

    # ---------------- Interaction ----------------
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            for idx, rect in enumerate(self._step_rects):
                if rect.contains(event.pos()):
                    self._show_context_menu(idx, event.globalPos())
                    return
        super().mousePressEvent(event)

    def _show_context_menu(self, step_index: int, global_pos: QPoint):
        menu = QMenu(self)
        label = self._labels[step_index]

        def setstate(s: StepState):
            self.set_step_state(step_index, s)

        menu.addAction(f"Mark '{label}' as Running", lambda: setstate(StepState.RUNNING))
        menu.addAction(f"Mark '{label}' as Completed", lambda: setstate(StepState.COMPLETED))
        menu.addAction(f"Mark '{label}' as Failed", lambda: setstate(StepState.FAILED))
        menu.addAction(f"Reset '{label}'", lambda: setstate(StepState.INACTIVE))

        menu.exec(global_pos)


# ---------------- Demo ----------------
def main():
    app = QApplication(sys.argv)

    progressbar = CustomProgressBar()
    progressbar.labels = ["Setup Docker", "Upload R1 & R2", "QC 1",  "UMI", "Cutadapt", "Fastp", "QC 2", "Read len", "Upload Ref Genome", "Read Mapping", "Site Analysis"]

    # buttons to simulate normal flow
    next_btn = QPushButton("Next")
    def advance():
        # find running step
        running_idx = None
        for i, st in enumerate(progressbar._states):
            if st == StepState.RUNNING:
                running_idx = i
                break

        if running_idx is None:
            # start with step 0 as running
            progressbar.set_step_state(0, StepState.RUNNING)
        else:
            # complete it
            progressbar.set_step_state(running_idx, StepState.COMPLETED)
            # start next if exists
            if running_idx + 1 < len(progressbar._states):
                progressbar.set_step_state(running_idx + 1, StepState.RUNNING)

    next_btn.clicked.connect(advance)

    reset_btn = QPushButton("Reset All")
    def reset():
        for i in range(len(progressbar._states)):
            progressbar.set_step_state(i, StepState.INACTIVE)
        progressbar._fill_width = 0.0
        progressbar.update()
    reset_btn.clicked.connect(reset)

    w = QWidget()
    lay = QVBoxLayout(w)
    lay.addWidget(progressbar)
    lay.addWidget(next_btn, alignment=Qt.AlignRight)
    lay.addWidget(reset_btn, alignment=Qt.AlignRight)
    w.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
