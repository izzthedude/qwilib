__all__ = [
    "IconButton",
    "RefreshButton",
    "NotificationButton",
    "FilterButton",
    "CreateButton",
    "CollapseButton",
    "InfoButton",
    "GridViewButton",
    "ListViewButton",
    "CancelButton",
    "ApplyButton",
    "ChangeButton",
    "ImportTasksFromButton",
    "ConnectParentsButton",
    "ToggleSidebarButton",
    "ToggleSearchContentsButton",
    "ToggleColumnsButton",
    "TogglePropertiesButton",
    "ToggleThemeButton",
]

from PySide6 import QtGui, QtWidgets

from qwilib import commons, enums


class IconButton(QtWidgets.QPushButton, commons.Toggleable, commons.Invisible):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self._icon_path = self._define_icon()
        self.setIcon(QtGui.QPixmap(self._icon_path))

    def _set_colored_icon(self, color: str = "white"):
        pixmap = QtGui.QPixmap(self._icon_path)
        painter = QtGui.QPainter(pixmap)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), QtGui.QColor(color))
        painter.end()

        self.setIcon(pixmap)

    def _define_icon(self) -> str:
        raise NotImplementedError("Override this method in child classes and return an icon.")


class RefreshButton(IconButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setToolTip("Refresh")

    def _define_icon(self) -> str:
        return enums.Icons.REFRESH_DEFAULT


class NotificationButton(IconButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setToolTip("Notifications")

    def _define_icon(self) -> str:
        return enums.Icons.NOTIFICATION_DEFAULT


class FilterButton(IconButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setToolTip("Filter")

    def _define_icon(self) -> str:
        return enums.Icons.FILTER_DEFAULT


class CreateButton(IconButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setToolTip("Create")

    def _define_icon(self) -> str:
        return enums.Icons.ADD_DEFAULT


class CollapseButton(IconButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setToolTip("Collapse")

    def _define_icon(self) -> str:
        return enums.Icons.COLLAPSE_DEFAULT


class InfoButton(IconButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setToolTip("Info")

    def _define_icon(self) -> str:
        return enums.Icons.INFO_DEFAULT


class GridViewButton(IconButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setToolTip("Grid View")

    def _define_icon(self) -> str:
        return enums.Icons.GRIDVIEW_DEFAULT


class ListViewButton(IconButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setToolTip("List View")

    def _define_icon(self) -> str:
        return enums.Icons.LISTVIEW_DEFAULT


class CancelButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.setText("Cancel")


class ApplyButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.setText("Apply")


class ChangeButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.setText("Change")


class ImportTasksFromButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.setText("Import Tasks from...")


class ConnectParentsButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.setText("Connect Parents")


class ToggleSidebarButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setText("Toggle Sidebar")
        self.setToolTip("Toggle the Sidebar")


class ToggleSearchContentsButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setText("Toggle Search Contents")
        self.setToolTip("Toggle the Search Contents")


class ToggleColumnsButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setText("Toggle Columns")
        self.setToolTip("Toggle the visibility of table columns")


class TogglePropertiesButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setText("Toggle Properties")
        self.setToolTip("Toggle the Properties bar")


class ToggleThemeButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent=parent)
        self.setText("Toggle Theme")
        self.setToolTip("Toggle the theme of the application")
