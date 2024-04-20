from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from GUI.nueva_tecla.EditarTeclaWindow import EditarTeclaWindow
from GUI.sesion.sesion_ui import Ui_Dialog_Sesion
from utils import guardar_muestra, error_window, info_window


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
            elif event.key() in [Qt.Key_Backspace, Qt.Key_Delete]:
                self.borrar_roca()
            elif tecla.isalnum():
                roca = self.muestra.mapa[tecla.upper()]
                if roca != "":
                    self.agregar_roca(roca)
        except Exception as e:
            error_window(self, e)

    def agregar_roca(self, roca):
        try:
            self.listwidgetRocas.insertItem(0, roca)
            self.incrementar_contador(roca)

            if self.listwidgetRocas.count() >= self.muestra.cantidad_lecturas:
                self.guardar()

                finalizarPopUp = QMessageBox(self)
                finalizarPopUp.setText(f"Sesión finalizada.\n"
                                       f"Se llegó a los {self.muestra.cantidad_lecturas} conteos.\n"
                                       f"Se procederá a calcular los resultados correspondientes.")
                finalizarPopUp.setIcon(QMessageBox.Information)
                finalizarPopUp.exec()

                mapa_fileName = self.muestra.exportar_datos()

                info_window(self, f"Se guardó la tabla de resultados en:\n{mapa_fileName}")

                self.close()
            else:
                self.guardar()
        except Exception as e:
            error_window(self, e)

    def incrementar_contador(self, componente):
        for i in range(self.tableView.rowCount()):
            if componente == self.tableView.item(i, 0).text():
                cantidad = int(self.tableView.item(i, 1).text()) + 1
                self.tableView.setItem(i, 1, QtWidgets.QTableWidgetItem(str(cantidad)))
                break

    def agregar_tecla(self):
        self.nueva_tecla_window = EditarTeclaWindow(self)
        self.nueva_tecla_window.show()

    def nueva_fila_contador(self, nombre_roca):
        ultima_fila = self.tableView.rowCount()
        self.tableView.insertRow(ultima_fila)
        self.tableView.setItem(ultima_fila, 0, QtWidgets.QTableWidgetItem(nombre_roca))
        self.tableView.setItem(ultima_fila, 1, QtWidgets.QTableWidgetItem('0'))
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()

    def borrar_roca(self):
        item = self.listwidgetRocas.takeItem(0)
        for i in range(self.tableView.rowCount()):
            if item.text() == self.tableView.item(i, 0).text():
                cantidad = int(self.tableView.item(i, 1).text()) - 1
                self.tableView.setItem(i, 1, QtWidgets.QTableWidgetItem(str(cantidad)))
                break

    def guardar(self):
        self.muestra.componentes = [self.listwidgetRocas.item(i).text() for i in range(self.listwidgetRocas.count())]
        guardar_muestra(self.muestra, self.muestra.fileName)
