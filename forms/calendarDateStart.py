from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from app.makeDates import set_start_date
from myCalendar import MyCalendar


class Calendar(QWidget):

    def __init__(self):
        super().__init__()

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
        self.selected_date = self.calendar.start_date
        set_start_date(self.select_date)

