import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QPushButton, QVBoxLayout


class Calendar(QWidget):

    def __init__(self):
        super().__init__()

        # Create a calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(50, 50, 200, 200)

        # Create a button to select the date range
        self.select_button = QPushButton('Select Date Range', self)
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
        # Get the selected start and end dates from the calendar widget
        start_date = self.calendar.selectedDate()
        end_date = self.calendar.selectedDateRange()[1]

        # Convert the start and end dates to strings in the format "yyyy-MM-dd"
        start_str = start_date.toString('yyyy-MM-dd')
        end_str = end_date.toString('yyyy-MM-dd')

        # Add all dates between the start and end dates to the set
        date = start_date
        while date <= end_date:
            self.selected_dates.add(date.toString('yyyy-MM-dd'))
            date = date.addDays(1)

        print('Selected Dates:', self.selected_dates)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calendar = Calendar()
    calendar.show()
    sys.exit(app.exec())
