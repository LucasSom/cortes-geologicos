import requests
from PyQt5 import QtWidgets

from GUI.menu_principal import MainWindow
from utils import info_window


def check_for_update(current_version, w):
    try:
        response = requests.get("https://api.github.com/repos/LucasSom/cortes-geologicos/releases/latest")
        latest_version = response.json()["tag_name"]

        if current_version < latest_version:
            notify_user(latest_version, w)
    except Exception as e:
        if type(e) == requests.exceptions.ConnectionError:
            info_window(w, "No se pudieron comprobar actualizaciones por problemas de conexión.")
        else:
            print(e)
            info_window(w, "No se pudieron comprobar actualizaciones por un problema desconocido.")


def notify_user(latest_version, w):
    info_window(w, f"Hay una nueva versión disponible: {latest_version}.\n"
                   f"Actualizar descargando de https://github.com/LucasSom/cortes-geologicos")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    check_for_update("v1.0.7", window)
    window.show()
    app.exec_()
