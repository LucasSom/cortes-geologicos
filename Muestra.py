import os

import pandas as pd


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
        path_dir = os.path.dirname(self.fileName)
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)

        df_new = pd.DataFrame(self.componentes, columns=["Muestra"])
        counts_df = pd.DataFrame(df_new["Muestra"].value_counts(normalize=True))
        df_new = counts_df.rename(columns={"proportion": self.nombre}).T

        # Cargar viejo CSV y concatenarlo
        file_path = os.path.join(path_dir, f"{self.localidad}.csv")
        if os.path.isfile(file_path):
            df_old = pd.read_csv(file_path, index_col=0)
            df_old.drop(["Promedio"], inplace=True)
            df_new = pd.concat([df_old, df_new]).fillna(0)

        # Calculo el promedio de cada columna
        promedio = df_new.mean()
        promedio["Muestra"] = "Promedio"
        df_promedio = pd.DataFrame(promedio).T.set_index("Muestra")
        df_new = pd.concat([df_new, df_promedio])

        mapa_fileName = os.path.join(path_dir, f"{self.localidad}.xlsx")
        df_new.to_excel(mapa_fileName, index_label='Muestra')
        return mapa_fileName
