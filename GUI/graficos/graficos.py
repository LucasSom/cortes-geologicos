from PyQt5.QtWidgets import QMainWindow
from matplotlib import pyplot as plt

from GUI.graficos.generar_graficos_ui import Ui_GraficosWindow
from diagrama_qfl import plot_qfl


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
        # El DataFrame tiene que tener como columnas: Index, Label, Q, F, L, Size, Color, Alpha, Marker
        # df = pd.DataFrame({
        #     'Index': [0, 1],
        #     'Label': ['Santa Rosa', 'Guatraché'],
        #     'Q': [0.3, 0.2],
        #     'F': [0.2, 0.3],
        #     'L': [0.5, 0.5],
        #     'Size': [10, 20],
        #     'Color': ['blue', 'green'],
        #     'Alpha': [1, 1],
        #     'Marker': ['x', 'o']
        # })
        # qfl = QFL(self, df)
        # # qfl = QFL(self, self.df)
        # qfl.Tri()
        # qfl.Explain()

        # convert counts to percent
        # self.df = self.df.div(self.df.sum(axis=1), axis=0) * 100
        # sum QFL types
        Q_columnas = [c for c in self.df.columns if c[1] == 'Q']
        cuarzos = self.df[Q_columnas].sum(axis=1)  # data_pct['Qm'] + data_pct['Qmu'] + data_pct['Qp']

        F_columnas = [c for c in self.df.columns if c[1] == 'F']
        feldespatos = self.df[F_columnas].sum(axis=1)  # data_pct['Plag'] + data_pct['Afsp']

        L_columnas = [c for c in self.df.columns if c[1] == 'L']
        liticos = self.df[L_columnas].sum(axis=1)  # data_pct['Lf']

        # the clay matrix can be None if not present
        O_columnas = [c for c in self.df.columns if c[1] == 'O']
        matrix = self.df[O_columnas].sum(axis=1)  # data_pct['PM+Cem']

        # for QFL top = quzrtz, left = feldspar, right = lithic
        # plot type options are 'Dickinson_1983', 'Pettijohn_1977' or 'blank'
        classified_data, plot = plot_qfl(self.df, top=cuarzos, left=feldespatos, right=liticos, matrix=matrix,
                                         plottype='Pettijohn_1977',
                                         toplab='Q', leftlab='F', rightlab='L', grid=True, color='r', size=15)
        plt.show()
        print(classified_data)

    def generar_QmFLQp(self):
        ...

    def relacion_Fp_F(self):
        ...

    def generar_LVLSLm(self):
        ...
