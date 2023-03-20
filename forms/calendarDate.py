from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QDesktopWidget

from datesCreation import set_end_date, set_start_date
from forms.myCalendar import MyCalendar


class CalendarEnd(QWidget):

    def __init__(self):
        super().__init__()
        self.center()

        # Create a calendar widget
        self.calendar = MyCalendar()
        self.calendar.setGeometry(50, 50, 200, 200)

        # Create a button to select the date range
        self.select_button = QPushButton('Сохранить дату', self)
        self.select_button.setGeometry(50, 300, 200, 50)
        self.select_button.clicked.connect(self.select_date)

        # Set the layout of the window
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.select_button)
        self.setLayout(layout)

    def select_date(self):
        selected_date_end = self.calendar.start_date
        set_end_date(selected_date_end)
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class CalendarStart(QWidget):

    def __init__(self):
        super().__init__()
        self.center()

        # Create a calendar widget
        self.calendar = MyCalendar()
        self.calendar.setGeometry(50, 50, 200, 200)

        # Create a button to select the date range
        self.select_button = QPushButton('Сохранить дату', self)
        self.select_button.setGeometry(50, 300, 200, 50)
        self.select_button.clicked.connect(self.select_date)

        # Set the layout of the window
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.select_button)
        self.setLayout(layout)

    def select_date(self):
        self.selected_date_start = self.calendar.start_date
        set_start_date(self.selected_date_start)
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
