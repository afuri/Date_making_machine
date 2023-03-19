import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel


# Унаследуем наш класс от простейшего графического примитива QWidget
class FirstForm(QMainWindow):
    def __init__(self, desktop_width, desktop_height):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю на
        # чтобы не перегружать инициализатор
        self.window_width = 800
        self.window_height = 600
        self.x_pos = (desktop_width - self.window_width) // 2
        self.y_pos = (desktop_height - self.window_height) // 2

        self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджет

        simple_width = self.window_width // 10
        simple_height = self.window_height // 10
        self.resize(self.window_width, self.window_height)
        self.move(self.x_pos, self.y_pos)
        # А также его заголовок
        self.setWindowTitle('Первая программа')
        # self.show_calendar(window_width, window_height)

        self.button_1 = QPushButton(self)
        self.button_1.resize(simple_width, simple_height // 2)
        self.button_1.move(self.window_width - 4 * simple_width, self.window_height - 2 * simple_height)
        self.button_1.setText("Календарь")
        self.button_1.clicked.connect(self.open_calendar)

        self.label = QLabel(self)
        self.label.resize(simple_width * 3, simple_height // 2) 
        self.label.setText("Пока никто не отправлял")
        self.label.move(50, 120)

    def open_calendar(self):
        self.calendar = SecondForm(self.x_pos, self.y_pos)
        self.calendar.show()     
        

class SecondForm(QWidget):
    def __init__(self, x_pos, y_pos):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        self.resize(460, 250)
        self.move(x_pos + 170, y_pos + 175)
        # А также его заголовок
        self.setWindowTitle('Календарь')
        self.show_calendar()  
 
    def show_calendar(self):
        # creating a QCalendarWidget object
        self.calendar = QCalendarWidget(self)
        self.calendar.adjustSize()
        # calendar_width = window_width // 2
        # calendar_height = window_height // 2
        # self.calendar.resize(calendar_width, calendar_height)
        # setting style sheet // change the color of calender if you want ..
        # self.calendar.setStyleSheet("background : blue;")
        # ensuring paint event
        self.calendar.repaint()


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    desktop = QApplication.desktop()
    desktop_width, desktop_height = desktop.width(), desktop.height()
    ex = FirstForm(desktop_width, desktop_height)
    
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())