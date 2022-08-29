__all__ = [
    "SplitContainer",
    "SplitHorizontalContainer",
    "SplitVerticalContainer"
]

from PySide6 import QtCore, QtWidgets

from qwilib.containers.layouts import *


class SplitContainer(QtWidgets.QSplitter):
    def __init__(self, orientation: QtCore.Qt.Orientation, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setHandleWidth(2)

        if orientation == QtCore.Qt.Horizontal:
            self.first_panel = VBoxContainer(self)
            self.second_panel = VBoxContainer(self)

        elif orientation == QtCore.Qt.Vertical:
            self.first_panel = HBoxContainer(self)
            self.second_panel = HBoxContainer(self)

        for child in self.findChildren(Container):
            index = self.indexOf(child)
            self.setCollapsible(index, False)

        self.addWidget(self.first_panel)
        self.addWidget(self.second_panel)

    def add_widget_to_first_panel(self, widget: QtWidgets.QWidget):
        self.first_panel.add_widget(widget)

    def add_widget_to_second_panel(self, widget: QtWidgets.QWidget):
        self.second_panel.add_widget(widget)

    def toggle_first_container(self):
        self.first_panel.toggle_visibility()

    def toggle_second_container(self):
        self.second_panel.toggle_visibility()

    def addWidget(self, widget: QtWidgets.QWidget):
        super().addWidget(widget)
        index = self.indexOf(widget)
        self.setCollapsible(index, False)


class SplitHorizontalContainer(SplitContainer):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(
            orientation=QtCore.Qt.Horizontal,
            parent=parent
        )


class SplitVerticalContainer(SplitContainer):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(
            orientation=QtCore.Qt.Vertical,
            parent=parent,
        )
