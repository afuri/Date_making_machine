
from PyQt5.QtWidgets import QPushButton, QSpinBox, QLineEdit
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget

from forms.dialogWindow import MyDialog

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_width = 800
        self.window_height = 600
        self.workday = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        self.filename = ''
        self.initUI()

    def initUI(self):
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle('Даты для КТП')
        self.center()

        self.mon = self.create_LabelDay('Понедельник', 30, 370)
        self.SpinBox_mon = self.create_SpinBox(135, 370)

        self.tue = self.create_LabelDay('Вторник', 30, 410)
        self.SpinBox_tue = self.create_SpinBox(135, 410)

        self.wen = self.create_LabelDay('Среда', 30, 450)
        self.SpinBox_wen = self.create_SpinBox(135, 450)

        self.thu = self.create_LabelDay('Четверг', 260, 370)
        self.SpinBox_thu = self.create_SpinBox(340, 370)

        self.fri = self.create_LabelDay('Пятница', 260, 410)
        self.SpinBox_fri = self.create_SpinBox(340, 410)

        self.sut = self.create_LabelDay('Суббота', 260, 450)
        self.SpinBox_sut = self.create_SpinBox(340, 450)
        
        self.label_1 = QLabel(self)
        self.label_1.setText("---------------------------------------------------------------------------------------")
        self.label_1.move(40, 490)
        self.label_1.adjustSize()

        self.label_2 = QLabel(self)
        self.label_2.setText("---------------------------------------------------------------------------------------")
        self.label_2.move(40, 310)
        self.label_2.adjustSize()

        self.name_label = QLabel(self)
        self.name_label.setText("Имя файла: ")
        self.name_label.move(30, 520)

        self.name_input = QLineEdit(self)
        self.name_input.move(135, 520)
        self.name_input.resize(300, 30)
        self.name_input.setClearButtonEnabled(True)

        self.btn = QPushButton('Создать файл', self)
        self.btn.resize(300, 30)
        self.btn.move(135, 560)
        self.btn.clicked.connect(self.make_file)


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