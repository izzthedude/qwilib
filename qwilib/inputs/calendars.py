__all__ = [
    "CalendarDateEdit"
]

from PySide6 import QtCore, QtWidgets


class CalendarDateEdit(QtWidgets.QDateEdit):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent=parent)

        self.setDisplayFormat("d MMMM yyyy")  # E.g 18 August 2022
        self.setDate(QtCore.QDate().currentDate())
        self.setCalendarPopup(True)
