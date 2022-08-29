__all__ = [
    "ScrollContainer",
    "ScrollVBoxContainer"
]

from PySide6 import QtCore, QtGui, QtWidgets

from qwilib.containers.layouts import *


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
