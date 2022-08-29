__all__ = [
    "FormWidget",
    "ComboBoxForm",
    "ProjectComboBox"
]

from PySide6 import QtCore, QtWidgets

from qwilib import inputs


class FormWidget(QtWidgets.QWidget):
    def __init__(self, label: str, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        layout = QtWidgets.QFormLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.widget = self._define_widget()
        label = label + ":"
        layout.addRow(label, self.widget)

    def _define_widget(self) -> QtWidgets.QWidget:
        raise NotImplementedError("Override this method and return some widget.")


class ComboBoxForm(FormWidget):
    combobox_selected = QtCore.Signal(int)

    def __init__(self, label: str, parent: QtWidgets.QWidget = None):
        super().__init__(label, parent)
        self.widget: QtWidgets.QComboBox = self.widget
        self.widget.currentIndexChanged.connect(self.combobox_selected.emit)

    def populate_combobox(self, items: list[str]):
        self.widget.addItems(items)

    def _define_widget(self) -> QtWidgets.QWidget:
        return inputs.NoScrollCombobox()


class ProjectComboBox(ComboBoxForm):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__("Project", parent=parent)
