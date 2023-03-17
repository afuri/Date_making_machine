import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget


# Унаследуем наш класс от простейшего графического примитива QWidget
class Example(QWidget):
    def __init__(self, desktop_width, desktop_height):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю на
        # чтобы не перегружать инициализатор
        self.initUI(desktop_width, desktop_height)

    def initUI(self, desktop_width, desktop_height):
        # Зададим размер и положение нашего виджета,
        
        window_width = desktop_width // 4
        window_height = desktop_height // 4
        self.resize(window_width, window_height)
        x_pos = (desktop_width - window_width) // 3
        y_pos = (desktop_height - window_height) // 2
        self.move(x_pos, y_pos)
        # А также его заголовок
        self.setWindowTitle('Первая программа')


if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    desktop = QApplication.desktop()
    desktop_width, desktop_height = desktop.width(), desktop.height()
    ex = Example(desktop_width, desktop_height)
    
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())