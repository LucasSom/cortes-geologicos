from PyQt5 import QtWidgets, QtCore


class RelacionWindow_Ui(object):
    def setupUi(self, RelacionWindow):
        RelacionWindow.setObjectName("MainWindow")
        RelacionWindow.resize(351, 71)
        RelacionWindow.setWindowTitle("Relación Fp/(Fp+Fk+Fm)")
        self.centralwidget = QtWidgets.QWidget(RelacionWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 311, 32))
        self.label.setObjectName("label")
        self.label.setText(f"Relación Fp/(Fp+Fk+Fm) promedio:\n{RelacionWindow.relacion}")

        RelacionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RelacionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 22))
        self.menubar.setObjectName("menubar")
        RelacionWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RelacionWindow)
        self.statusbar.setObjectName("statusbar")
        RelacionWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(RelacionWindow)


class RelacionWindow(QtWidgets.QMainWindow, RelacionWindow_Ui):
    def __init__(self, relacion):
        QtWidgets.QMainWindow.__init__(self)
        self.relacion = relacion
        self.setupUi(self)
