from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets

from qwilib import commons


class Container(QtWidgets.QWidget, commons.Toggleable):
    resized = QtCore.Signal(int, int)

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        layout = self._define_layout()
        self.setLayout(layout)

    def add_widget(self, widget: QtWidgets.QWidget):
        self.layout().addWidget(widget)

    def add_layout(self, layout: QtWidgets.QLayout):
        self.layout().addLayout(layout)

    def set_alignment(self, alignment: QtCore.Qt.AlignmentFlag):
        self.layout().setAlignment(alignment)

    def setLayout(self, layout: QtWidgets.QLayout):
        layout.setContentsMargins(0, 0, 0, 0)
        super(Container, self).setLayout(layout)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resized.emit(self.geometry().width(), self.geometry().height())

    def _define_layout(self) -> QtWidgets.QLayout:
        raise NotImplementedError("Override this method and return some layout.")


class VBoxContainer(Container):
    def _define_layout(self) -> QtWidgets.QLayout:
        return QtWidgets.QVBoxLayout()


class HBoxContainer(Container):
    def _define_layout(self) -> QtWidgets.QLayout:
        return QtWidgets.QHBoxLayout()


class SplitContainer(QtWidgets.QSplitter):
    def __init__(self, orientation: QtCore.Qt.Orientation, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setHandleWidth(2)

        if orientation == QtCore.Qt.Horizontal:
            self.first_panel = VBoxContainer(self)
            self.second_panel = VBoxContainer(self)

        elif orientation == QtCore.Qt.Vertical:
            self.first_panel = HBoxContainer(self)
            self.second_panel = HBoxContainer(self)

        for child in self.findChildren(Container):
            index = self.indexOf(child)
            self.setCollapsible(index, False)

        self.addWidget(self.first_panel)
        self.addWidget(self.second_panel)

    def add_widget_to_first_panel(self, widget: QtWidgets.QWidget):
        self.first_panel.add_widget(widget)

    def add_widget_to_second_panel(self, widget: QtWidgets.QWidget):
        self.second_panel.add_widget(widget)

    def toggle_first_container(self):
        self.first_panel.toggle_visibility()

    def toggle_second_container(self):
        self.second_panel.toggle_visibility()

    def addWidget(self, widget: QtWidgets.QWidget):
        super().addWidget(widget)
        index = self.indexOf(widget)
        self.setCollapsible(index, False)


class SplitHorizontalContainer(SplitContainer):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(
            orientation=QtCore.Qt.Horizontal,
            parent=parent
        )


class SplitVerticalContainer(SplitContainer):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(
            orientation=QtCore.Qt.Vertical,
            parent=parent,
        )


class SpreadHorizontalContainer(HBoxContainer):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        self.left_zone = HBoxContainer(self)
        self.left_zone.set_alignment(QtCore.Qt.AlignLeft)

        self.center_zone = HBoxContainer(self)
        self.center_zone.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.center_zone.set_alignment(QtCore.Qt.AlignCenter)

        self.right_zone = HBoxContainer(self)
        self.right_zone.set_alignment(QtCore.Qt.AlignRight)

        self.add_widget(self.left_zone)
        self.add_widget(self.center_zone)
        self.add_widget(self.right_zone)

    def add_widget_left(self, widget: QtWidgets.QWidget = None):
        self.left_zone.add_widget(widget)

    def add_widget_center(self, widget: QtWidgets.QWidget = None):
        self.center_zone.add_widget(widget)

    def add_widget_right(self, widget: QtWidgets.QWidget = None):
        self.right_zone.add_widget(widget)


class CorneredTabContainer(QtWidgets.QTabWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        self.corner_container = HBoxContainer(self)
        self.setCornerWidget(self.corner_container, QtCore.Qt.TopRightCorner)

    def add_widget_corner(self, widget: QtWidgets.QWidget):
        self.corner_container.add_widget(widget)


class FormContainer(Container):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        self.self_layout: QtWidgets.QGridLayout = self.layout()
        self.separator = ":"

    def add_row(self, label: str, widget: QtWidgets.QWidget):
        row_count = self.layout().rowCount()

        row_label = QtWidgets.QLabel(label, self)
        separator_label = QtWidgets.QLabel(self.separator, self)

        self.layout().addWidget(row_label, row_count, 1)
        self.layout().addWidget(separator_label, row_count, 2)
        self.layout().addWidget(widget, row_count, 3)

    def set_separator(self, text: str):
        self.separator = text

    def get_column_width(self, column: int):
        return self.layout().itemAtPosition(1, column).geometry().width()

    def _define_layout(self) -> QtWidgets.QLayout:
        return QtWidgets.QGridLayout()


class ScrollContainer(QtWidgets.QScrollArea):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.central_widget = self._define_container()

    def __init_subclass__(cls, *args, **kwargs):
        # Source: https://stackoverflow.com/questions/71183263/automatically-call-method-after-init-in-child-class
        super().__init_subclass__(*args, **kwargs)

        def sub_init(self, *args, init=cls.__init__, **kwargs):
            init(self, *args, **kwargs)
            if cls == type(self):
                self.setWidget(self.central_widget)

        cls.__init__ = sub_init

    def add_widget(self, widget: QtWidgets.QWidget):
        self.central_widget.add_widget(widget)

    def resizeEvent(self, arg__1: QtGui.QResizeEvent):
        scrollbar_w = 0
        if self.verticalScrollBar().isVisible():
            scrollbar_w = self.verticalScrollBar().width()

        area_w = self.width() - scrollbar_w - 2
        self.widget().setFixedWidth(area_w)

    def _define_container(self) -> Container:
        raise NotImplementedError("Override this method and return some central_widget.")


class ScrollVBoxContainer(ScrollContainer):
    def _define_container(self) -> Container:
        return VBoxContainer(self)
