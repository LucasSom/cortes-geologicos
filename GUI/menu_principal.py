import os.path

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from GUI.graficos.graficos import GraficosWindow
from GUI.nueva_muestra.NuevaMuestra import NuevaMuestraWindow
from GUI.sesion.Sesion import SesionWindow
from GUI.menu_principal_ui import Ui_MainWindow
from utils import cargar_archivo_muestra


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        self.nueva_muestra_w = None
        self.cargar_muestra_w = None
        self.sesion_window = None
        self.graficos_window = None
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_nueva_muestra)
        self.pushButton_2.clicked.connect(self.cargar_muestra)
        self.cargarTablaBoton.clicked.connect(self.cargar_tabla)

    def show_nueva_muestra(self, checked):
        if self.nueva_muestra_w is None:
            self.nueva_muestra_w = NuevaMuestraWindow()
            self.nueva_muestra_w.show()
        else:
            self.nueva_muestra_w = None  # Discard reference and close window.

    def openFileNameDialog(self, tipo='mtra'):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName = None

        if tipo == 'mtra':
            fileName, _ = QFileDialog.getOpenFileName(self, "Cargar muestra", os.path.curdir,
                                                      "All Files (*);;Muestras (*.mtra)", options=options)
        elif tipo == 'csv':
            fileName, _ = QFileDialog.getOpenFileName(self, "Cargar tabla CSV", os.path.curdir,
                                                      "All Files (*);;CSV (*.csv)", options=options)

        if fileName:
            return fileName
        return None

    def cargar_muestra(self, checked):
        fileName = self.openFileNameDialog()
        if fileName is not None:
            muestra = cargar_archivo_muestra(fileName)
            if self.sesion_window is None:
                self.sesion_window = SesionWindow(muestra)
                self.sesion_window.show()
            else:
                self.sesion_window = None

    def cargar_tabla(self, checked):
        fileName = self.openFileNameDialog(tipo='csv')
        if fileName is not None:
            df = pd.read_csv(fileName)
            if self.graficos_window is None:
                self.graficos_window = GraficosWindow(df)
                self.graficos_window.show()
            else:
                self.graficos_window = None


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
