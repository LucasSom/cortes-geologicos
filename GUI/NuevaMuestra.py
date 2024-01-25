from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from GUI.nueva_muestra_ui import Ui_NuevaMuestraWindow
from Muestra import Muestra
from utils import guardar_muestra


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

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Guardar muestra", "../muestras",
                                                  "All Files (*);;Muestras (*.mtra)", options=options)
        if fileName:
            print(fileName)
            return fileName
        return None

    def aceptar(self):
        nueva_muestra = Muestra(self.nombre.text(),
                                self.fecha.date().toPyDate(),
                                self.localidad.text(),
                                self.numero.value(),
                                self.operador.text(),
                                self.cantidad_lecturas.value(),
                                self.observaciones.toPlainText(),
                                self.mapa)
        fileName = self.saveFileDialog()
        if fileName is not None:
            guardar_muestra(nueva_muestra, fileName, verbose=True)
        self.close()

    def cancelar(self):
        self.close()
