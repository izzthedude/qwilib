__all__ = [
    "IconAndName"
]

from PySide6 import QtCore, QtWidgets

from qwilib import containers, displays, enums


class IconAndName(containers.HBoxContainer):
    def __init__(self, name: str, icon_path: str = enums.Icons.DEFAULT_PROFILE, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        icon = displays.SizedPixmapLabel(icon_path, parent=self)
        name_display = displays.VCenterAlignedLabel(name, parent=self)
        self.set_alignment(QtCore.Qt.AlignLeft)
        self.add_widget(icon)
        self.add_widget(name_display)
