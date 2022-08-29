__all__ = [
    "NoScrollCombobox"
]

from PySide6 import QtWidgets, QtGui


class NoScrollCombobox(QtWidgets.QComboBox):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

    def wheelEvent(self, event: QtGui.QWheelEvent):
        pass
