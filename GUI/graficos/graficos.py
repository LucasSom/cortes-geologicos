from PyQt5.QtWidgets import QMainWindow
from matplotlib import pyplot as plt

from GUI.graficos.generar_graficos_ui import Ui_GraficosWindow
from diagrama import plot_diagrama
from utils import filtrar_tipo_roca


class GraficosWindow(QMainWindow, Ui_GraficosWindow):
    def __init__(self, df):
        QMainWindow.__init__(self)
        self.df = df
        # self.df.index.name = 'Muestra'
        # s = df.T["Promedio"]
        # self.df = pd.DataFrame({'Muestra': list(s.index), 'Promedio': list(s)})
        self.setupUi(self)

        self.QFL_boton.clicked.connect(self.generar_qfl)
        self.QmFLQp_boton.clicked.connect(self.generar_QmFLQp)
        self.relacion_Fp_F_Boton.clicked.connect(self.relacion_Fp_F)
        self.LVLSLm_boton.clicked.connect(self.generar_LVLSLm)

    def generar_qfl(self):
        cuarzos = filtrar_tipo_roca(self.df, tipo='Q')
        feldespatos = filtrar_tipo_roca(self.df, tipo='F')
        liticos = filtrar_tipo_roca(self.df, tipo='L')
        # the clay matrix can be None if not present
        matrix = filtrar_tipo_roca(self.df, tipo='O')

        classified_data, plot = plot_diagrama(self.df, top=cuarzos, left=feldespatos, right=liticos, matrix=matrix,
                                              plot_type='Pettijohn_1977',
                                              top_label='Q', left_label='F', right_label='L',
                                              grid=True, color='r', size=15)
        plt.show()
        print(classified_data)

    def generar_QmFLQp(self):
        cuarzos_monocristalinos = filtrar_tipo_roca(self.df, tipo='Qm')
        feldespatos = filtrar_tipo_roca(self.df, tipo='F')
        liticos = filtrar_tipo_roca(self.df, tipo='L')
        cuarzos_policristalinos = filtrar_tipo_roca(self.df, tipo='Qp')

        classified_data, plot = plot_diagrama(self.df,
                                              top=cuarzos_monocristalinos,
                                              left=feldespatos,
                                              right=liticos + cuarzos_policristalinos,
                                              matrix=None,
                                              plot_type='blank',
                                              top_label='Qm', left_label='F', right_label='L+Qp',
                                              grid=True, color='r', size=15)
        plt.show()

    def relacion_Fp_F(self):
        ...

    def generar_LVLSLm(self):
        ...
