from GUI.sesion_ui import Ui_Dialog
from PyQt5 import QtWidgets


class SesionWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, nombre, mapa):
        super(SesionWindow, self).__init__()
        self.nombre = nombre
        self.mapa = mapa
        self.setupUi(self)
