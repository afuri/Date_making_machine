import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QListWidget, QVBoxLayout, QPushButton


class Calendar(QWidget):

    def __init__(self):
        super().__init__()

        # Create a calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(50, 50, 200, 200)

        # Create a list widget to display selected dates
        self.date_list = QListWidget(self)
        self.date_list.setGeometry(300, 50, 200, 200)

        # Create a button to add selected dates to the list
        self.add_button = QPushButton('Add Selected Dates', self)
        self.add_button.setGeometry(50, 300, 200, 50)
        self.add_button.clicked.connect(self.add_dates)

        # Set the layout of the window
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.date_list)
        layout.addWidget(self.add_button)
        self.setLayout(layout)

        # Keep track of selected dates
        self.selected_dates = set()

    def add_dates(self):
        # Get the selected dates from the calendar widget
        selected = self.calendar.selectedDates()

        # Add each selected date to the list widget
        for date in selected:
            self.selected_dates.add(date.toString('yyyy-MM-dd'))
            self.date_list.addItem(date.toString('yyyy-MM-dd'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calendar = Calendar()
    calendar.show()
    sys.exit(app.exec_())
