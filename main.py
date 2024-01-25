import sys

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication


def main_menu(argv):
    app = QApplication(argv)
    app.setStyle('Plastic style')
    # app.setStyleSheet('')
    # app.setFont(QFont(''))
    # app.setWindowIcon(QIcon(''))
    # menu = MainMenu()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main_menu(sys.argv)

