from PyQt5 import QtWidgets

from GUI.sesion_ui import Ui_Dialog


class SesionWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, nombre, mapa):
        super(SesionWindow, self).__init__()
        self.nombre = nombre
        self.mapa = mapa
        self.setupUi(self)
