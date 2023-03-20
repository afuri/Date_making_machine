import sys
from PyQt5.QtWidgets import QApplication

from forms.mainForm import MainForm


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())