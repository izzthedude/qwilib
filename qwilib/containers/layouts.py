__all__ = [
    "Container",
    "VBoxContainer",
    "HBoxContainer",
    "SpreadHorizontalContainer",
    "FormContainer"
]

from PySide6 import QtCore, QtWidgets

from qwilib import commons


class Container(QtWidgets.QWidget, commons.Toggleable):
    resized = QtCore.Signal(int, int)

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        layout = self._define_layout()
        self.setLayout(layout)

    def add_widget(self, widget: QtWidgets.QWidget):
        self.layout().addWidget(widget)

    def add_layout(self, layout: QtWidgets.QLayout):
        self.layout().addLayout(layout)

    def set_alignment(self, alignment: QtCore.Qt.AlignmentFlag):
        self.layout().setAlignment(alignment)

    def setLayout(self, layout: QtWidgets.QLayout):
        layout.setContentsMargins(0, 0, 0, 0)
        super(Container, self).setLayout(layout)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resized.emit(self.geometry().width(), self.geometry().height())

    def _define_layout(self) -> QtWidgets.QLayout:
        raise NotImplementedError("Override this method and return some layout.")


class VBoxContainer(Container):
    def _define_layout(self) -> QtWidgets.QLayout:
        return QtWidgets.QVBoxLayout()


class HBoxContainer(Container):
    def _define_layout(self) -> QtWidgets.QLayout:
        return QtWidgets.QHBoxLayout()


class SpreadHorizontalContainer(HBoxContainer):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        self.left_zone = HBoxContainer(self)
        self.left_zone.set_alignment(QtCore.Qt.AlignLeft)

        self.center_zone = HBoxContainer(self)
        self.center_zone.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.center_zone.set_alignment(QtCore.Qt.AlignCenter)

        self.right_zone = HBoxContainer(self)
        self.right_zone.set_alignment(QtCore.Qt.AlignRight)

        self.add_widget(self.left_zone)
        self.add_widget(self.center_zone)
        self.add_widget(self.right_zone)

    def add_widget_left(self, widget: QtWidgets.QWidget = None):
        self.left_zone.add_widget(widget)

    def add_widget_center(self, widget: QtWidgets.QWidget = None):
        self.center_zone.add_widget(widget)

    def add_widget_right(self, widget: QtWidgets.QWidget = None):
        self.right_zone.add_widget(widget)


class FormContainer(Container):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        self.self_layout: QtWidgets.QGridLayout = self.layout()
        self.separator = ":"

    def add_row(self, label: str, widget: QtWidgets.QWidget):
        row_count = self.layout().rowCount()

        row_label = QtWidgets.QLabel(label, self)
        separator_label = QtWidgets.QLabel(self.separator, self)

        self.layout().addWidget(row_label, row_count, 1)
        self.layout().addWidget(separator_label, row_count, 2)
        self.layout().addWidget(widget, row_count, 3)

    def set_separator(self, text: str):
        self.separator = text

    def get_column_width(self, column: int):
        return self.layout().itemAtPosition(1, column).geometry().width()

    def _define_layout(self) -> QtWidgets.QLayout:
        return QtWidgets.QGridLayout()
