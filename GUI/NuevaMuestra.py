from PyQt5 import QtWidgets
from GUI.nueva_muestra_ui import Ui_NuevaMuestraWindow
from Muestra import Muestra
from utils import save_pickle


class NuevaMuestraWindow(QtWidgets.QMainWindow, Ui_NuevaMuestraWindow):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.mapa = {}
        self.setupUi(self)
        self.cancelar_aceptar_boton.accepted.connect(self.aceptar)
        self.cancelar_aceptar_boton.rejected.connect(self.cancelar)

    def aceptar(self):
        nueva_muestra = Muestra(self.nombre.text(),
                                self.fecha.date().toPyDate(),
                                self.localidad.text(),
                                self.numero.value(),
                                self.operador.text(),
                                self.cantidad_lecturas.value(),
                                self.observaciones.toPlainText(),
                                self.mapa)
        save_pickle(nueva_muestra, "muestra_prueba.pkl", verbose=True)

    def cancelar(self):
        self.close()
