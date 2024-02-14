import os

import pandas as pd
from PyQt5.QtWidgets import QFileDialog

from GUI.editar_mapa.editar_mapa_ui import Ui_MainWindow
from utils import file_extension


class EditarMapaWindow(Ui_MainWindow):
    def __init__(self, parent=None):
        self.mapa = parent.mapa
        super(EditarMapaWindow, self).__init__(parent.mapa)
        self.parent = parent
        self.botonGuardar.clicked.connect(self.guardar)

    def guardar(self):
        self.mapa = {
            "A": self.text_A.text(),
            "S": self.text_S.text(),
            "D": self.text_D.text(),
            "F": self.text_F.text(),
            "G": self.text_G.text(),
            "H": self.text_H.text(),
            "J": self.text_J.text(),
            "K": self.text_K.text(),
            "L": self.text_L.text(),
            "Q": self.text_Q.text(),
            "W": self.text_W.text(),
            "E": self.text_E.text(),
            "R": self.text_R.text(),
            "T": self.text_T.text(),
            "Y": self.text_Y.text(),
            "U": self.text_U.text(),
            "I": self.text_I.text(),
            "O": self.text_O.text(),
            "P": self.text_P.text(),
            "Z": self.text_Z.text(),
            "X": self.text_X.text(),
            "C": self.text_C.text(),
            "V": self.text_V.text(),
            "B": self.text_B.text(),
            "N": self.text_N.text(),
            "M": self.text_M.text(),
            "0": self.text_0.text(),
            "1": self.text_1.text(),
            "2": self.text_2.text(),
            "3": self.text_3.text(),
            "4": self.text_4.text(),
            "5": self.text_5.text(),
            "6": self.text_6.text(),
            "7": self.text_7.text(),
            "8": self.text_8.text(),
            "9": self.text_9.text(),
        }
        if self.parent is not None:
            self.parent.mapa = self.mapa

            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self, "Guardar mapa de teclas", os.path.curdir,
                                                      "CSV (*.csv);;All Files (*)", options=options)
            df = pd.DataFrame({tecla: [roca] for tecla, roca in self.mapa.items()})
            df.to_csv(fileName if file_extension(fileName) == '.csv' else fileName + '.csv', index=False)

            # self.parent.setupUi(self.parent)
        self.close()

