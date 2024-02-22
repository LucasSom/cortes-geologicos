from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from GUI.nueva_tecla.NuevaTeclaWindow import NuevaTeclaWindow
from GUI.sesion.sesion_ui import Ui_Dialog_Sesion
from utils import guardar_muestra, error_window


class SesionWindow(QtWidgets.QDialog, Ui_Dialog_Sesion, QtWidgets.QWidget):
    def __init__(self, muestra):
        try:
            super(SesionWindow, self).__init__()
            self.muestra = muestra
            self.nueva_tecla_window = None
            self.setupUi(self)

            self.deshacerButton.clicked.connect(self.borrar_roca)
            self.agregarTeclaButton.clicked.connect(self.agregar_tecla)
            self.aceptar_cancelar.accepted.connect(self.guardar)
        except Exception as e:
            error_window(self, e)

    def keyPressEvent(self, event):
        try:
            tecla = event.text()
            if event.key() == Qt.Key_Escape:
                self.cancelar()
            elif tecla.isalnum():
                roca = self.muestra.mapa[tecla.upper()]
                if roca != "":
                    self.agregar_roca(roca)
        except Exception as e:
            error_window(self, e)

    def agregar_roca(self, roca):
        try:
            self.listwidgetRocas.insertItem(0, roca)
            if self.listwidgetRocas.count() >= self.muestra.cantidad_lecturas:
                self.guardar()

                finalizarPopUp = QMessageBox(self)
                finalizarPopUp.setText(f"Sesión finalizada.\n"
                                       f"Se llegó a las {self.muestra.cantidad_lecturas} muestras.\n"
                                       f"Se procederá a calcular los resultados correspondientes.")
                finalizarPopUp.setIcon(QMessageBox.Information)
                finalizarPopUp.exec()

                mapa_fileName = self.muestra.exportar_datos()

                guardadoPopUp = QMessageBox(self)
                guardadoPopUp.setText(f"Se guardó la tabla de resultados en:\n"
                                      f"{mapa_fileName}\n")
                guardadoPopUp.setIcon(QMessageBox.Information)
                guardadoPopUp.exec()

                self.close()
        except Exception as e:
            error_window(self, e)

    def agregar_tecla(self):
        self.nueva_tecla_window = NuevaTeclaWindow(self)
        self.nueva_tecla_window.show()

    def borrar_roca(self):
        self.listwidgetRocas.takeItem(0)

    def guardar(self):
        self.muestra.componentes = [self.listwidgetRocas.item(i).text() for i in range(self.listwidgetRocas.count())]
        guardar_muestra(self.muestra, self.muestra.fileName)
