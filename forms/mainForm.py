
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QSpinBox, QLineEdit
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from forms.dialogWindow import MyDialog, SimpleDialog
from db.dbCreation import myDB
from forms.calendarSomeDates import Calendar
from app.datetotable import get_list_of_holidays

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_width = 800
        self.window_height = 600
        self.workday = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        self.filename = ''
        self.initUI()
        ex = myDB()
        ex.create_table()


    def initUI(self):
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle('Даты для КТП')
        self.center()
        self.db_show()

        self.pixmap = QPixmap('assets/pict.png')
        # Если картинки нет, то QPixmap будет пустым, 
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(20, 20)
        self.image.resize(760, 180) 
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

        self.mon = self.create_LabelDay('Понедельник', 30, 350)
        self.SpinBox_mon = self.create_SpinBox(135, 350)

        self.tue = self.create_LabelDay('Вторник', 30, 390)
        self.SpinBox_tue = self.create_SpinBox(135, 390)

        self.wen = self.create_LabelDay('Среда', 30, 430)
        self.SpinBox_wen = self.create_SpinBox(135, 430)

        self.thu = self.create_LabelDay('Четверг', 260, 350)
        self.SpinBox_thu = self.create_SpinBox(340, 350)

        self.fri = self.create_LabelDay('Пятница', 260, 390)
        self.SpinBox_fri = self.create_SpinBox(340, 390)

        self.sut = self.create_LabelDay('Суббота', 260, 430)
        self.SpinBox_sut = self.create_SpinBox(340, 430)
        
        self.label_1 = QLabel(self)
        self.label_1.setText("---------------------------------------------------------------------------------------")
        self.label_1.move(40, 470)
        self.label_1.adjustSize()

        self.label_2 = QLabel(self)
        self.label_2.setText("---------------------------------------------------------------------------------------")
        self.label_2.move(40, 310)
        self.label_2.adjustSize()

        self.name_label = QLabel(self)
        self.name_label.setText("Имя файла: ")
        self.name_label.move(30, 500)

        self.name_input = QLineEdit(self)
        self.name_input.move(135, 500)
        self.name_input.resize(300, 30)
        self.name_input.setClearButtonEnabled(True)

        self.btn = QPushButton('Создать файл', self)
        self.btn.resize(300, 30)
        self.btn.move(135, 540)
        self.btn.clicked.connect(self.make_file)

        self.btn_2 = QPushButton('Редактировать выходные', self)
        self.btn_2.resize(300, 30)
        self.btn_2.move(480, 220)
        self.btn_2.clicked.connect(self.show_dates)

        self.btn_3 = QPushButton('Очистить таблицу', self)
        self.btn_3.resize(300, 30)
        self.btn_3.move(480, 540)
        self.btn_3.clicked.connect(self.update_date)

    def make_file(self):
        self.workday[0] = self.SpinBox_mon.text()  # Получим текст из поля ввода
        self.workday[1] = self.SpinBox_tue.text()
        self.workday[2] = self.SpinBox_wen.text()
        self.workday[3] = self.SpinBox_thu.text()
        self.workday[4] = self.SpinBox_fri.text()
        self.workday[5] = self.SpinBox_sut.text()
        self.filename = self.name_input.text()
        dlg = MyDialog(self.filename, self.workday)
        dlg.exec()
    
    def create_SpinBox(self, x, y):
        self = QSpinBox(self)
        self.move(x, y)
        self.setMinimum(0)
        self.setMaximum(7)
        self.setProperty("value", 0)
        return self

    def create_LabelDay(self, text, x, y):
        self = QLabel(self)
        self.setText(text)
        self.move(x, y)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def db_show(self):
        holidays = get_list_of_holidays()
        self.table = QTableWidget(self)
        self.table.setRowCount(len(holidays))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["День", 'Месяц', 'Год'])
        for i, value in enumerate(holidays):
            item_name = QTableWidgetItem(value[0])
            item_code = QTableWidgetItem(value[1])
            item_color = QTableWidgetItem(value[2])
            self.table.setItem(i, 0, item_name)
            self.table.setItem(i, 1, item_code)
            self.table.setItem(i, 2, item_color)
        self.table.move(460, 270)
        self.table.resize(330, 260)
        self.table.repaint()


    def show_dates(self):
        self.calendar = Calendar()
        self.calendar.show()

        
    def update_date(self):
        dlg_2 = SimpleDialog()
        dlg_2.exec()

        
        
        
        