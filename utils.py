import os
import pickle

import pandas as pd


def file_extension(p):
    return os.path.splitext(p)[1]


def guardar_muestra(obj, file_name: str, verbose=False):
    if file_extension(file_name) != '.mtra':
        file_name += '.mtra'

    directory = os.path.dirname(file_name)
    if not os.path.isdir(directory) and directory != '':
        os.makedirs(directory)
        if verbose: print("Created directory:", directory)

    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)
        if verbose: print("Saved as:", file_name)


def cargar_archivo_muestra(file_name: str, verbose=False):
    if file_extension(file_name) != '.mtra':
        file_name += '.mtra'

    with open(file_name, 'rb') as f:
        p = pickle.load(f)
        if verbose: print("Loaded file:", f)
        return p


def filtrar_tipo_roca(df: pd.DataFrame, tipo: str) -> pd.DataFrame:
    columnas = [c for c in df.columns if c[1:len(tipo) + 1] == tipo]
    return df[columnas].sum(axis=1)
