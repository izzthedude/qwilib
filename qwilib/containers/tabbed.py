__all__ = [
    "CorneredTabContainer"
]

from PySide6 import QtCore, QtWidgets

from qwilib import containers


class CorneredTabContainer(QtWidgets.QTabWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        self.corner_container = containers.HBoxContainer(self)
        self.setCornerWidget(self.corner_container, QtCore.Qt.TopRightCorner)

    def add_widget_corner(self, widget: QtWidgets.QWidget):
        self.corner_container.add_widget(widget)
