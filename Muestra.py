import os
from collections import Counter

import pandas as pd
from pandas import Series


class Muestra:
    def __init__(self, nombre, fecha, localidad, operador, cantidad_lecturas, observaciones, mapa, fileName):
        self.nombre = nombre
        self.fecha = fecha
        self.localidad = localidad
        self.operador = operador
        self.cantidad_lecturas = cantidad_lecturas
        self.observaciones = observaciones
        self.mapa = mapa
        self.fileName = fileName
        self.componentes = []

    def exportar_datos(self):
        path_dir = os.path.join(os.path.dirname(self.fileName), "tablas")
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)

        df = pd.DataFrame(self.componentes, columns=["Muestra"])
        df = pd.DataFrame(df.value_counts(normalize=True)).rename(columns={"proportion": self.nombre}).T
        df.to_csv(os.path.join(path_dir, f"{self.localidad}.csv"))
