from PyQt5 import QtWidgets

from GUI.sesion_ui import Ui_Dialog


class SesionWindow(QtWidgets.QDialog, Ui_Dialog, QtWidgets.QWidget):
    def __init__(self, nombre, mapa):
        super(SesionWindow, self).__init__()
        self.nombre = nombre
        self.mapa = mapa
        self.setupUi(self)

        self.deshacerButton.clicked.connect(self.borrar_roca)

    def keyPressEvent(self, event):
        self.agregar_roca(self.mapa[event.text().upper()])

    def agregar_roca(self, roca):
        self.listwidgetRocas.insertItem(0, roca)

    def borrar_roca(self):
        self.listwidgetRocas.takeItem(0)
