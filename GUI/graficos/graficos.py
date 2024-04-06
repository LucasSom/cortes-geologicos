import pandas as pd
from PyQt5.QtWidgets import QMainWindow
from matplotlib import pyplot as plt

from GUI.graficos.generar_graficos_ui import Ui_GraficosWindow
from diagrama import plot_diagrama
from utils import filtrar_tipo_roca, error_window, info_window


class GraficosWindow(QMainWindow, Ui_GraficosWindow):
    def __init__(self, df, fileName):
        QMainWindow.__init__(self)
        self.relacion_window = None
        self.fileName = fileName
        self.df = df
        self.setupUi(self)

        self.QFL_boton_dickinson.clicked.connect(self.generar_qfl_dickinson)
        self.QFL_boton_folk.clicked.connect(self.generar_qfl_folk)
        self.QFL_boton_garzanti.clicked.connect(self.generar_qfl_garzanti)
        self.QmFLQp_boton.clicked.connect(self.generar_QmFLQp)
        self.relacion_Fp_F_Boton.clicked.connect(self.relacion_Fp_F)
        self.LVLSLm_boton.clicked.connect(self.generar_LvLsLm)

    def generar_qfl_dickinson(self):
        self.generar_qfl(clasificacion='Dickinson_1983_QFL')

    def generar_qfl_folk(self):
        self.generar_qfl(clasificacion='Folk')

    def generar_qfl_garzanti(self):
        self.generar_qfl(clasificacion='Garzanti_2019')

    def generar_qfl(self, clasificacion):
        try:
            cuarzos = filtrar_tipo_roca(self.df, tipo='Q')
            feldespatos = filtrar_tipo_roca(self.df, tipo='F')
            liticos = filtrar_tipo_roca(self.df, tipo='L')
            # the clay matrix can be None if not present
            matrix = filtrar_tipo_roca(self.df, tipo='O')

            classified_data, plot = plot_diagrama(self.df, top=cuarzos, left=feldespatos, right=liticos, matrix=matrix,
                                                  plot_type=clasificacion,
                                                  top_label='Q', left_label='F', right_label='L')
            plt.show()
            print(classified_data)

            df = pd.concat([cuarzos, feldespatos, liticos], axis=1)
            df.columns = ["Q", "F", "L"]
            df.index = self.df["Muestra"]
            df[f"Total-{clasificacion}"] = df.sum(axis=1)
            export_path = f"{self.fileName}-QFL.xlsx"
            df.to_excel(export_path)

            info_window(self, f"Tabla guardada en {export_path}")
        except Exception as e:
            error_window(self, e)

    def generar_QmFLQp(self):
        try:
            cuarzos_monocristalinos = filtrar_tipo_roca(self.df, tipo='Qm')
            feldespatos = filtrar_tipo_roca(self.df, tipo='F')
            liticos = filtrar_tipo_roca(self.df, tipo='L')
            cuarzos_policristalinos = filtrar_tipo_roca(self.df, tipo='Qp')

            classified_data, plot = plot_diagrama(self.df,
                                                  top=cuarzos_monocristalinos,
                                                  left=feldespatos,
                                                  right=liticos + cuarzos_policristalinos,
                                                  matrix=None,
                                                  plot_type='Dickinson_1983_QmFLQp',
                                                  top_label='Qm', left_label='F', right_label='L+Qp')
            plt.show()

            df = pd.concat([cuarzos_monocristalinos, feldespatos, liticos + cuarzos_policristalinos], axis=1)
            df.columns = ["Qm", "F", "L+Qp"]
            df.index = self.df["Muestra"]
            df["Total"] = df.sum(axis=1)
            export_path = f"{self.fileName}-QmFLQp.xlsx"
            df.to_excel(export_path)

            info_window(self, f"Tabla guardada en {export_path}")
        except Exception as e:
            error_window(self, e)

    def relacion_Fp_F(self):
        try:
            Fp = filtrar_tipo_roca(self.df, tipo='Fp')
            Fk = filtrar_tipo_roca(self.df, tipo='Fk')
            Fm = filtrar_tipo_roca(self.df, tipo='Fm')

            df_relacion = self.df.copy()
            df_relacion['relacion_Fp_F'] = (Fp/(Fp+Fk+Fm)).fillna(0)
            df_relacion = df_relacion.set_index('Muestra')

            export_path = f"{self.fileName}-Fp_F.xlsx"
            df_relacion.to_excel(export_path)

            info_window(self, f"Tabla guardada en {export_path}")
        except Exception as e:
            error_window(self, e)

    def generar_LvLsLm(self):
        try:
            liticos_volcanicos = filtrar_tipo_roca(self.df, tipo='Lv')
            liticos_sedimentarios = filtrar_tipo_roca(self.df, tipo='Ls')
            liticos_metamorficos = filtrar_tipo_roca(self.df, tipo='Lm')

            classified_data, plot = plot_diagrama(self.df,
                                                  top=liticos_volcanicos,
                                                  left=liticos_sedimentarios,
                                                  right=liticos_metamorficos,
                                                  plot_type='blank',
                                                  top_label='Lv', left_label='Ls', right_label='Lm')
            plt.show()

            df = pd.concat([liticos_volcanicos, liticos_sedimentarios, liticos_metamorficos], axis=1)
            df.columns = ["Lv", "Ls", "Lm"]
            df.index = self.df["Muestra"]
            df["Total"] = df.sum(axis=1)
            export_path = f"{self.fileName}-LvLsLm.xlsx"
            df.to_excel(export_path)

            info_window(self, f"Tabla guardada en {export_path}")

        except Exception as e:
            error_window(self, e)
