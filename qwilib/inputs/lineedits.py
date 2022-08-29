__all__ = [
    "SearchLineEdit"
]

from PySide6 import QtWidgets


class SearchLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setPlaceholderText("Type here to search...")
