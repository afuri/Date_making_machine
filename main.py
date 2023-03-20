import sys
from PyQt5.QtWidgets import QApplication

from forms.mainForm import MainForm


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # desktop = QApplication.desktop()
    # desktop_width, desktop_height = desktop.width(), desktop.height()
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())