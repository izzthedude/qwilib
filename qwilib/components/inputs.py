__all__ = [
    "SearchAndFilter",
    "SearchAndCreate"
]

from PySide6 import QtCore, QtWidgets

from qwilib import containers, inputs


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
