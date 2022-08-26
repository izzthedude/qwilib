from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets

from qwilib import enums


class AlignedLabel(QtWidgets.QLabel):
    def __init__(self, text: str = "", parent: QtWidgets.QWidget = None):
        super().__init__(text=text, parent=parent)

        alignment = self._define_alignment()
        self.setAlignment(alignment)

    def _define_alignment(self) -> QtCore.Qt.Alignment | QtCore.Qt.AlignmentFlag:
        raise NotImplementedError


class VCenterAlignedLabel(AlignedLabel):
    def _define_alignment(self) -> QtCore.Qt.Alignment | QtCore.Qt.AlignmentFlag:
        return QtCore.Qt.AlignVCenter


class CenterAlignedLabel(AlignedLabel):
    def _define_alignment(self) -> QtCore.Qt.Alignment | QtCore.Qt.AlignmentFlag:
        return QtCore.Qt.AlignCenter


class LeftAlignedLabel(AlignedLabel):
    def _define_alignment(self) -> QtCore.Qt.Alignment | QtCore.Qt.AlignmentFlag:
        return QtCore.Qt.AlignLeft


class RightAlignedLabel(AlignedLabel):
    def _define_alignment(self) -> QtCore.Qt.Alignment | QtCore.Qt.AlignmentFlag:
        return QtCore.Qt.AlignRight


class UsernameLabel(VCenterAlignedLabel):
    def __init__(self, name: str, username: str, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        self.setText(f"{name}\n{username}")


class PixmapLabel(CenterAlignedLabel):
    def __init__(self, icon_path: str, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        pixmap = QtGui.QPixmap(icon_path)
        self.setPixmap(pixmap)


class SizedPixmapLabel(CenterAlignedLabel):
    def __init__(self, icon_path: str, size: int = enums.IconSizes.MEDIUM, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.pixmap_size = size

        self.setPixmap(icon_path)

    def setPixmap(self, arg__1: QtGui.QPixmap | QtGui.QImage | str) -> None:
        pixmap = QtGui.QPixmap(arg__1)
        pixmap = pixmap.scaledToHeight(self.pixmap_size, QtCore.Qt.SmoothTransformation)
        super().setPixmap(pixmap)


class DebugLabel(CenterAlignedLabel):
    def __init__(self, text: str = "Debug", parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        self.setStyleSheet("border: 1px solid red;")
        self.setText(text)
