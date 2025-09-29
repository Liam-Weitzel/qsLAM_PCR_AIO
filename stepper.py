import os
import math
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class CustomVariantAnimation(QVariantAnimation):
    def updateCurrentValue(self, value):
        pass


class CustomProgressBar(QWidget):
    stepsChanged = Signal(list)
    valueChanged = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._labels = []
        self._value = 0  # logical target value (int)
        self._display_progress = 0.0  # animated float progress (0..N)

        # animation will interpolate self._display_progress
        self._animation = CustomVariantAnimation(self)
        self._animation.valueChanged.connect(self._on_anim_value)
        self._animation.finished.connect(self._on_anim_finished)

        self._step_rects = []  # store the circle rects for hit-testing

    def _on_anim_value(self, v):
        # QVariantAnimation emits a QVariant; convert to float and repaint
        try:
            self._display_progress = float(v)
        except Exception:
            self._display_progress = v
        self.update()

    def _on_anim_finished(self):
        # ensure we land exactly on integer target
        self._display_progress = float(self._value)
        self.update()

    def get_labels(self):
        return self._labels

    def set_labels(self, labels):
        self._labels = labels[:]
        self.stepsChanged.emit(self._labels)

    labels = Property(list, fget=get_labels, fset=set_labels, notify=stepsChanged)

    def get_value(self):
        return self._value

    def set_value(self, value):
        if 0 <= value < len(self.labels) + 1:
            # set logical target immediately (other code may rely on it)
            self._value = value
            self.valueChanged.emit(value)

            # animate display_progress from current to the integer target
            start = self._display_progress
            end = float(value)
            if start == end:
                # nothing to animate
                return
            self._animation.stop()
            self._animation.setStartValue(start)
            self._animation.setEndValue(end)

            # duration proportional to distance (ms), clamp to sensible range
            dist = abs(end - start)
            duration = int(350 * dist)
            if duration < 1:
                self._display_progress = end
                self.update()
                return
            self._animation.setDuration(duration)
            self._animation.start()

    value = Property(int, fget=get_value, fset=set_value, notify=valueChanged)

    def sizeHint(self):
        return QSize(320, 120)

    def paintEvent(self, event):
        grey = QColor("#777")
        grey2 = QColor("#dfe3e4")
        blue = QColor("#2183dd")
        green = QColor("#009900")
        white = QColor("#fff")

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)

        height = 5
        offset = 10
        painter.fillRect(self.rect(), white)

        # track / background
        busy_rect = QRect(0, 0, self.width(), height)
        busy_rect.adjust(offset, 0, -offset, 0)
        busy_rect.moveCenter(self.rect().center())
        painter.fillRect(busy_rect, grey2)

        number_of_steps = len(self.labels)
        if number_of_steps == 0:
            return

        step_width = busy_rect.width() / number_of_steps

        # use animated display_progress for drawing
        progress = max(0.0, min(self._display_progress, float(number_of_steps)))
        # blue bar extends from left up to progress * step_width (progress==1 -> center of step1)
        blue_width = progress * step_width
        r_busy = QRect(busy_rect.left(), busy_rect.top(), int(blue_width), height)
        painter.fillRect(r_busy, blue)

        # prepare for circles / labels
        x = offset + step_width / 2
        y = busy_rect.center().y()
        radius = 10

        font_text = painter.font()
        font_icon = QFont("Font Awesome 5 Free")
        font_icon.setPixelSize(radius)

        r = QRect(0, 0, int(1.5 * radius), int(1.5 * radius))
        fm = QFontMetrics(font_text)

        self._step_rects.clear()

        # which integer steps are considered "filled" by current progress?
        filled_steps = int(math.floor(progress + 1e-9))  # 0..N
        active_step = filled_steps + 1  # next step index (1-based)

        for i, text in enumerate(self.labels, 1):
            r.moveCenter(QPoint(int(x), int(y)))
            self._step_rects.append(QRect(r))  # save clickable rect

            if i <= filled_steps:
                # fully filled step (green)
                pen = QPen(green)
                pen.setWidth(3)
                painter.setPen(pen)
                painter.setBrush(green)
                painter.drawEllipse(r)
                painter.setFont(font_icon)
                painter.setPen(white)
                painter.drawText(r, Qt.AlignCenter, chr(0xF00C))
                painter.setPen(green)

            else:
                # not-yet-filled (outline). Mark "active" for the upcoming step.
                is_active = (active_step == i)
                pen = QPen(grey if is_active else grey2)
                pen.setWidth(3)
                painter.setPen(pen)
                painter.setBrush(white)
                painter.drawEllipse(r)
                painter.setPen(blue if is_active else QColor("black"))

            rect = fm.boundingRect(text)
            rect.moveCenter(QPoint(int(x), int(y + 2 * radius)))
            painter.setFont(font_text)
            painter.drawText(rect, Qt.AlignCenter, text)

            x += step_width

    # ---------- context menu handling ----------
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            for idx, rect in enumerate(self._step_rects):
                if rect.contains(event.pos()):
                    self._show_context_menu(idx, event.globalPos())
                    return
        super().mousePressEvent(event)

    def _show_context_menu(self, step_index: int, global_pos: QPoint):
        """Dynamic actions based on the step index/label."""
        menu = QMenu(self)
        label = self.labels[step_index] if 0 <= step_index < len(self.labels) else f"Step {step_index+1}"

        # dynamic: example actions
        menu.addAction(f"Info about '{label}'", lambda: self._action_info(step_index))
        menu.addSeparator()
        for i in range(1, 4):
            menu.addAction(f"Custom Action {i} for '{label}'", lambda i=i: self._custom_action(step_index, i))

        menu.exec(global_pos)

    def _action_info(self, step_index):
        QMessageBox.information(self, "Step Info", f"This is step {step_index + 1}: {self.labels[step_index]}")

    def _custom_action(self, step_index, i):
        QMessageBox.information(self, "Custom Action", f"Action {i} triggered on step {step_index + 1}")


def main():
    import sys
    app = QApplication(sys.argv)

    # optional: load Font Awesome if present
    _id = QFontDatabase.addApplicationFont(os.path.join(CURRENT_DIR, "fa-solid-900.ttf"))
    print("Loaded font families:", QFontDatabase.applicationFontFamilies(_id))

    progressbar = CustomProgressBar()
    progressbar.labels = ["Step One", "Step Two", "Step Three", "Complete"]

    button = QPushButton("Next Step")
    button.clicked.connect(lambda: setattr(progressbar, 'value', (progressbar.value + 1) % (len(progressbar.labels) + 1)))

    w = QWidget()
    lay = QVBoxLayout(w)
    lay.addWidget(progressbar)
    lay.addWidget(button, alignment=Qt.AlignRight)
    w.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
