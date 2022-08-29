__all__ = [
    "WindowView"
]

from PySide6 import QtCore, QtGui, QtWidgets

from qwilib import containers, enums


class WindowView(containers.VBoxContainer):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)

        self.setWindowFlag(QtCore.Qt.Window)
        self.setWindowIcon(QtGui.QPixmap(enums.Icons.APP_LOGO))

        title = self._define_title()
        self.setWindowTitle(title)

    def __init_subclass__(cls, *args, **kwargs):
        # Source: https://stackoverflow.com/questions/71183263/automatically-call-method-after-init-in-child-class
        super().__init_subclass__(*args, **kwargs)

        def sub_init(self, *args, init=cls.__init__, **kwargs):
            init(self, *args, **kwargs)
            if cls == type(self):
                size = self._define_size()
                self.resize(size)

        cls.__init__ = sub_init

    def _define_title(self) -> str:
        raise NotImplementedError("Override this method and return some window title.")

    def _define_size(self) -> QtCore.QSize:
        raise NotImplementedError("Override this method and return some QSize.")
