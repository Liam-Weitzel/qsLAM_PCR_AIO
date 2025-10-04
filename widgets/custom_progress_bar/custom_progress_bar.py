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
        # each step is {"label": str, "actions": [(name, callable), ...]}
        self._steps: list[dict] = []
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

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self._steps:
            number_of_steps = len(self._steps)
            step_width = (self.width() - 20) / number_of_steps
            completed_count = 0
            for st in self._states:
                if st == StepState.COMPLETED:
                    completed_count += 1
                else:
                    break
            target_width = (completed_count - 0.5) * step_width if completed_count > 0 else 0
            self._fill_width = target_width
            self.update()

    # ---------------- API ----------------
    def set_labels(self, steps: list):
        """
        steps: list of str OR list of dicts
        dict format: { "label": str, "actions": [(name, func), ...] }
        """
        normalized = []
        for s in steps:
            if isinstance(s, str):
                normalized.append({"label": s, "actions": []})
            elif isinstance(s, dict):
                normalized.append({"label": s["label"], "actions": s.get("actions", [])})
            else:
                raise ValueError("Steps must be str or dict with keys 'label' and optional 'actions'")

        self._steps = normalized
        self._states = [StepState.INACTIVE] * len(self._steps)
        self.stepsChanged.emit([s["label"] for s in self._steps])
        self.update()

    def get_labels(self):
        return [s["label"] for s in self._steps]

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
        idx = -1
        for i, st in enumerate(self._states):
            if st == StepState.COMPLETED:
                idx = i
            else:
                break
        return idx

    def reset(self):
        for i in range(len(self._states)):
            self.set_step_state(i, StepState.INACTIVE)
        self._fill_width = 0.0
        self.update()

    def set_step_state_by_label(self, label: str, state: StepState):
        for i, step in enumerate(self._steps):
            if step["label"] == label:
                self.set_step_state(i, state)
                return
        raise ValueError(f"No step with label '{label}' found")

    def get_step_state_by_label(self, label: str) -> StepState:
        for i, step in enumerate(self._steps):
            if step["label"] == label:
                return self.get_step_state(i)
        raise ValueError(f"No step with label '{label}' found")

    # ---------------- internal helpers ----------------
    def _update_animation(self):
        if not self._steps:
            return
        number_of_steps = len(self._steps)
        step_width = (self.width() - 20) / number_of_steps  # track width - margins

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
        grey2 = QColor("#dfe3e4")
        blue = QColor("#2183dd")
        green = QColor("#009900")
        red = QColor("red")
        white = QColor("#fff")

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.fillRect(self.rect(), white)

        if not self._steps:
            return

        # ----------------- setup busy bar -----------------
        height = 5
        offset = 10
        busy_rect = QRect(0, 0, self.width(), height)
        busy_rect.adjust(offset, 0, -offset, 0)
        busy_rect.moveCenter(self.rect().center())
        painter.fillRect(busy_rect, grey2)

        # blue fill
        if self._fill_width > 0:
            r_busy = QRect(busy_rect.left(), busy_rect.top(), int(self._fill_width), height)
            painter.fillRect(r_busy, blue)

        # ----------------- adaptive sizing -----------------
        number_of_steps = len(self._steps)
        step_width = busy_rect.width() / number_of_steps
        x = busy_rect.left() + step_width / 2
        y = busy_rect.center().y()

        # circle radius
        max_radius = min(13, (step_width - 10) / 2)
        min_radius = 6
        radius = max(min_radius, int(max_radius))

        # font scaling
        font_text = painter.font()
        font_size = font_text.pointSize()
        fm = QFontMetrics(font_text)
        for step in self._steps:
            label_width = fm.horizontalAdvance(step["label"])
            while label_width > step_width - 4 and font_size > 6:
                font_size -= 1
                font_text.setPointSize(font_size)
                fm = QFontMetrics(font_text)
                label_width = fm.horizontalAdvance(step["label"])
        painter.setFont(font_text)

        r = QRect(0, 0, int(1.5 * radius), int(1.5 * radius))
        self._step_rects.clear()

        for i, (step, state) in enumerate(zip(self._steps, self._states)):
            text = step["label"]
            r.moveCenter(QPoint(int(x), int(y)))
            self._step_rects.append(QRect(r))

            # draw circle
            if state == StepState.COMPLETED:
                painter.setPen(QPen(green, 3))
                painter.setBrush(green)
                painter.drawEllipse(r)
                painter.setPen(white)
                painter.drawText(r, Qt.AlignCenter, "✔")

            elif state == StepState.RUNNING:
                painter.setPen(QPen(blue, 3))
                painter.setBrush(white)
                painter.drawEllipse(r)
                tri = QPolygon([
                    QPoint(r.center().x() - 3, r.center().y() - 5),
                    QPoint(r.center().x() - 3, r.center().y() + 5),
                    QPoint(r.center().x() + 6, r.center().y()),
                ])
                painter.setBrush(blue)
                painter.setPen(Qt.NoPen)
                painter.drawPolygon(tri)

            elif state == StepState.FAILED:
                painter.setPen(QPen(red, 3))
                painter.setBrush(red)
                painter.drawEllipse(r)
                painter.setPen(white)
                painter.drawText(r, Qt.AlignCenter, "✗")

            else:  # INACTIVE
                painter.setPen(QPen(grey2, 3))
                painter.setBrush(white)
                painter.drawEllipse(r)

            # label
            elided_text = fm.elidedText(text, Qt.ElideRight, int(step_width - 4))
            rect = fm.boundingRect(elided_text)
            rect.moveCenter(QPoint(int(x), int(y + 2 * radius)))
            painter.setPen(blue if state == StepState.RUNNING else QColor("black"))
            painter.drawText(rect, Qt.AlignCenter, elided_text)

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
        step = self._steps[step_index]

        # custom actions
        if step["actions"]:
            menu.addSeparator()
            for action_name, func in step["actions"]:
                menu.addAction(action_name, func)

        menu.setStyleSheet("""
            QMenu {
                background-color: white;
                color: black;
                border: 1px solid black;
                padding: 5px;
                border-radius: 4px;
            }
            QMenu::item {
                padding: 4px 20px 4px 20px;
            }
            QMenu::item:selected {
                background-color: #cce6ff;
                color: black;
            }
            QMenu::separator {
                height: 1px;
                background: #aaa;
                margin: 5px 0;
            }
        """)

        menu.exec(global_pos)
