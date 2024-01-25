from PyQt5 import QtWidgets

from GUI.CargarMuestra import CargarMuestraWindow
from GUI.NuevaMuestra import NuevaMuestraWindow
from GUI.menu_principal_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        self.nueva_muestra_w = None
        self.cargar_muestra_w = None
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_nueva_muestra)
        self.pushButton_2.clicked.connect(self.show_cargar_muestra)

    def show_nueva_muestra(self, checked):
        if self.nueva_muestra_w is None:
            self.nueva_muestra_w = NuevaMuestraWindow()
            self.nueva_muestra_w.show()
        else:
            self.nueva_muestra_w = None  # Discard reference and close window.

    def show_cargar_muestra(self, checked):
        if self.cargar_muestra_w is None:
            self.cargar_muestra_w = CargarMuestraWindow()
            self.cargar_muestra_w.show()
        else:
            self.cargar_muestra_w = None  # Discard reference and close window.


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
