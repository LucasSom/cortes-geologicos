import os.path

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from GUI.editar_mapa.EditarMapaWindow import EditarMapaWindow
from GUI.sesion.Sesion import SesionWindow
from GUI.nueva_muestra.nueva_muestra_ui import Ui_NuevaMuestraWindow
from Muestra import Muestra
from utils import guardar_muestra


class NuevaMuestraWindow(QtWidgets.QMainWindow, Ui_NuevaMuestraWindow):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.editar_mapa_w = None
        self.sesion_window = None
        self.mapa = {}
        self.setupUi(self)
        self.cancelar_aceptar_boton.accepted.connect(self.aceptar)
        self.cancelar_aceptar_boton.rejected.connect(self.cancelar)
        self.editar_mapa_boton.clicked.connect(self.editar_mapa)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Guardar muestra", os.path.curdir,
                                                  "All Files (*);;Muestras (*.mtra)", options=options)
        if fileName:
            return fileName
        return None

    def aceptar(self):
        fileName = self.saveFileDialog()
        nueva_muestra = Muestra(self.nombre.text(),
                                self.fecha.date().toPyDate(),
                                self.localidad.text(),
                                self.operador.text(),
                                self.cantidad_lecturas.value(),
                                self.observaciones.toPlainText(),
                                self.editar_mapa_w.mapa,
                                fileName)
        if fileName is not None:
            guardar_muestra(nueva_muestra, fileName, verbose=True)

        if self.sesion_window is None:
            self.sesion_window = SesionWindow(nueva_muestra)
            self.sesion_window.show()
        else:
            self.sesion_window = None
        self.close()

    def cancelar(self):
        self.close()

    def editar_mapa(self):
        if self.editar_mapa_w is None:
            self.editar_mapa_w = EditarMapaWindow()
            self.editar_mapa_w.show()
        else:
            self.editar_mapa_w = None  # Discard reference and close window.
