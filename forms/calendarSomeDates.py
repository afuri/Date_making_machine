import datetime as dt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QDesktopWidget

from datesCreation import set_holidays
from forms.myCalendar import MyCalendar


class Calendar(QWidget):

    def __init__(self):
        super().__init__()
        self.center()
        # Create a calendar widget
        self.calendar = MyCalendar()
        self.calendar.setGeometry(50, 50, 200, 200)

        # Create a button to select the date range
        self.select_button = QPushButton('Сохранить даты', self)
        self.select_button.setGeometry(50, 300, 200, 50)
        self.select_button.clicked.connect(self.select_range)

        # Set the layout of the window
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.select_button)
        self.setLayout(layout)

        # Keep track of the selected date range
        self.selected_dates = set()

    def select_range(self):
        self.selected_dates.add(self.calendar.start_date)
        while self.calendar.start_date != self.calendar.finish_date:
            self.calendar.start_date += dt.timedelta(days=1)
            self.selected_dates.add(self.calendar.start_date)
        set_holidays(self.selected_dates)
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
