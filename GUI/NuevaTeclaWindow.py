from GUI.nueva_tecla_ui import Ui_Dialog_Nueva_Tecla
from PyQt5 import QtWidgets


class NuevaTeclaWindow(QtWidgets.QDialog, Ui_Dialog_Nueva_Tecla):
    def __init__(self, parent=None):
        super(NuevaTeclaWindow, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.aceptar_cancelar.accepted.connect(self.insertar_tecla)

    def insertar_tecla(self):
        tecla = self.tecla_input.text().upper()
        roca = self.roca_input.text()
        self.parent.muestra.mapa[tecla] = roca

        self.parent.imprimir_lista_teclas()

        self.close()
