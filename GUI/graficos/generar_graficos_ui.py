# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/graficos/generar_graficos.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraficosWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 491)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.QFL_boton = QtWidgets.QPushButton(self.centralwidget)
        self.QFL_boton.setGeometry(QtCore.QRect(20, 20, 281, 91))
        self.QFL_boton.setObjectName("QFL_boton")

        self.QmFLQp_boton = QtWidgets.QPushButton(self.centralwidget)
        self.QmFLQp_boton.setGeometry(QtCore.QRect(20, 130, 281, 91))
        self.QmFLQp_boton.setObjectName("QmFLQp_boton")

        self.relacion_Fp_F_Boton = QtWidgets.QPushButton(self.centralwidget)
        self.relacion_Fp_F_Boton.setGeometry(QtCore.QRect(20, 350, 281, 91))
        self.relacion_Fp_F_Boton.setObjectName("relacion_Fp_F_Boton")

        self.LVLSLm_boton = QtWidgets.QPushButton(self.centralwidget)
        self.LVLSLm_boton.setGeometry(QtCore.QRect(20, 240, 281, 91))
        self.LVLSLm_boton.setObjectName("LVLSLm_boton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 322, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generar gráficos"))
        self.QFL_boton.setText(_translate("MainWindow", "Generar QFL"))
        self.QmFLQp_boton.setText(_translate("MainWindow", "Generar Qm-F-(L+Qp)"))
        self.relacion_Fp_F_Boton.setText(_translate("MainWindow", "Calcular relación Fp/(Fp+Fk+Fm)"))
        self.LVLSLm_boton.setText(_translate("MainWindow", "Generar LV-LS-Lm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GraficosWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())