from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from GUI.sesion_ui import Ui_Dialog
from utils import guardar_muestra


class SesionWindow(QtWidgets.QDialog, Ui_Dialog, QtWidgets.QWidget):
    def __init__(self, muestra):
        super(SesionWindow, self).__init__()
        self.muestra = muestra
        self.setupUi(self)

        self.deshacerButton.clicked.connect(self.borrar_roca)
        self.aceptar_cancelar.accepted.connect(self.guardar)
        # self.aceptar_cancelar.rejected.connect(self.cancelar)

    def keyPressEvent(self, event):
        tecla = event.text()
        if event.key() == Qt.Key_Escape:
            self.cancelar()
        elif tecla.isalnum():
            roca = self.muestra.mapa[tecla.upper()]
            self.agregar_roca(roca)

    def agregar_roca(self, roca):
        self.listwidgetRocas.insertItem(0, roca)

    def borrar_roca(self):
        self.listwidgetRocas.takeItem(0)

    def guardar(self):
        self.muestra.componentes = [self.listwidgetRocas.item(i).text() for i in range(self.listwidgetRocas.count())]
        guardar_muestra(self.muestra, self.muestra.fileName)

    # def cancelar(self):
    #     cancelarPopUp = QMessageBox(self)
    #     cancelarPopUp.setText("¿Cerrar sin guardar?")
    #     cancelarPopUp.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     cancelarPopUp.setIcon(QMessageBox.Warning)
    #     cancelarPopUp.exec()
