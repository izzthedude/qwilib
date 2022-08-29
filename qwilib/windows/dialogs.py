__all__ = [
    "ModalWindow"
]

from PySide6 import QtCore, QtWidgets

from qwilib.windows.windows import WindowView


class ModalWindow(WindowView):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent=parent)

        self.setWindowModality(QtCore.Qt.WindowModal)
