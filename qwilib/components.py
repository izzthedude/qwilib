from PySide6 import QtCore
from PySide6 import QtWidgets

from qwilib import containers, inputs, displays, enums


class SearchAndFilter(containers.HBoxContainer):
    lineedit_changed = QtCore.Signal(str)
    filter_clicked = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)

        self.search_lineedit = inputs.SearchLineEdit(self)
        self.search_lineedit.textChanged.connect(self.lineedit_changed.emit)

        self.filter_btn = inputs.FilterButton(self)
        self.filter_btn.clicked.connect(self.filter_clicked.emit)

        self.add_widget(self.search_lineedit)
        self.add_widget(self.filter_btn)


class SearchAndCreate(containers.HBoxContainer):
    lineedit_changed = QtCore.Signal(str)
    create_clicked = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)

        self.search_lineedit = inputs.SearchLineEdit(self)
        self.search_lineedit.textChanged.connect(self.lineedit_changed.emit)

        self.create_btn = inputs.CreateButton(self)
        self.create_btn.clicked.connect(self.create_clicked.emit)

        self.add_widget(self.search_lineedit)
        self.add_widget(self.create_btn)


class IconAndName(containers.HBoxContainer):
    def __init__(self, name: str, icon_path: str = enums.Icons.DEFAULT_PROFILE, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        icon = displays.SizedPixmapLabel(icon_path, parent=self)
        name_display = displays.VCenterAlignedLabel(name, parent=self)
        self.set_alignment(QtCore.Qt.AlignLeft)
        self.add_widget(icon)
        self.add_widget(name_display)
