from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

from app.toexcel import write_to_excel
from app.worklist import get_workdays_list


class MyDialog(QDialog):
    def __init__(self, filename, workday):
        super().__init__()
        self.filename = filename
        self.workday = workday

        self.setWindowTitle("Внимание!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        if self.filename == '':
            self.filename = 'Default'
        message = QLabel(f"В текущей папке будет создан файл {self.filename}.xlsx с датами Ваших уроков. Подтвердить?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept(self) -> None:
        write_to_excel(get_workdays_list(self.workday), self.filename)
        self.close()