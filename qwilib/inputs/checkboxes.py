__all__ = [
    "ShowMyTaskCheckBox"
]

from PySide6 import QtWidgets


class ShowMyTaskCheckBox(QtWidgets.QCheckBox):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setText("Show My Task only")
