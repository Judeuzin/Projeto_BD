# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Guilda.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Guilda(object):
    def setupUi(self, Tela_Guilda):
        Tela_Guilda.setObjectName("Tela_Guilda")
        Tela_Guilda.resize(650, 500)
        self.label_nome = QtWidgets.QLabel(Tela_Guilda)
        self.label_nome.setGeometry(QtCore.QRect(40, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_nome.setFont(font)
        self.label_nome.setObjectName("label_nome")
        self.verticalLayoutWidget = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 140, 161, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_nome_jogador_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nome_jogador_1.setObjectName("label_nome_jogador_1")
        self.verticalLayout.addWidget(self.label_nome_jogador_1)
        self.label_nivel_jogador_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nivel_jogador_1.setObjectName("label_nivel_jogador_1")
        self.verticalLayout.addWidget(self.label_nivel_jogador_1)
        self.label_integrantes = QtWidgets.QLabel(Tela_Guilda)
        self.label_integrantes.setGeometry(QtCore.QRect(40, 80, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_integrantes.setFont(font)
        self.label_integrantes.setObjectName("label_integrantes")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 180, 160, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_nome_jogador_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_nome_jogador_2.setObjectName("label_nome_jogador_2")
        self.verticalLayout_2.addWidget(self.label_nome_jogador_2)
        self.label_nivel_jogador_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_nivel_jogador_2.setObjectName("label_nivel_jogador_2")
        self.verticalLayout_2.addWidget(self.label_nivel_jogador_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 260, 160, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_nome_jogador_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_nome_jogador_4.setObjectName("label_nome_jogador_4")
        self.verticalLayout_3.addWidget(self.label_nome_jogador_4)
        self.label_nivel_jogador_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_nivel_jogador_4.setObjectName("label_nivel_jogador_4")
        self.verticalLayout_3.addWidget(self.label_nivel_jogador_4)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(40, 220, 160, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_nome_jogador_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_nome_jogador_3.setObjectName("label_nome_jogador_3")
        self.verticalLayout_4.addWidget(self.label_nome_jogador_3)
        self.label_nivel_jogador_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_nivel_jogador_3.setObjectName("label_nivel_jogador_3")
        self.verticalLayout_4.addWidget(self.label_nivel_jogador_3)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(360, 180, 160, 41))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_nome_jogador_9 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_nome_jogador_9.setObjectName("label_nome_jogador_9")
        self.verticalLayout_9.addWidget(self.label_nome_jogador_9)
        self.label_nivel_jogador_9 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_nivel_jogador_9.setObjectName("label_nivel_jogador_9")
        self.verticalLayout_9.addWidget(self.label_nivel_jogador_9)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(360, 260, 160, 41))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_nome_jogador_11 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_nome_jogador_11.setObjectName("label_nome_jogador_11")
        self.verticalLayout_10.addWidget(self.label_nome_jogador_11)
        self.label_nivel_jogador_11 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_nivel_jogador_11.setObjectName("label_nivel_jogador_11")
        self.verticalLayout_10.addWidget(self.label_nivel_jogador_11)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(360, 220, 160, 41))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_nome_jogador_10 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_nome_jogador_10.setObjectName("label_nome_jogador_10")
        self.verticalLayout_11.addWidget(self.label_nome_jogador_10)
        self.label_nivel_jogador_10 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_nivel_jogador_10.setObjectName("label_nivel_jogador_10")
        self.verticalLayout_11.addWidget(self.label_nivel_jogador_10)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(360, 140, 160, 41))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_nome_jogador_8 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_nome_jogador_8.setObjectName("label_nome_jogador_8")
        self.verticalLayout_12.addWidget(self.label_nome_jogador_8)
        self.label_nivel_jogador_8 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_nivel_jogador_8.setObjectName("label_nivel_jogador_8")
        self.verticalLayout_12.addWidget(self.label_nivel_jogador_8)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(40, 300, 160, 41))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_nome_jogador_5 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_nome_jogador_5.setObjectName("label_nome_jogador_5")
        self.verticalLayout_13.addWidget(self.label_nome_jogador_5)
        self.label_nivel_jogador_5 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_nivel_jogador_5.setObjectName("label_nivel_jogador_5")
        self.verticalLayout_13.addWidget(self.label_nivel_jogador_5)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(40, 380, 160, 41))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_nome_jogador_7 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_nome_jogador_7.setObjectName("label_nome_jogador_7")
        self.verticalLayout_14.addWidget(self.label_nome_jogador_7)
        self.label_nivel_jogador_7 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_nivel_jogador_7.setObjectName("label_nivel_jogador_7")
        self.verticalLayout_14.addWidget(self.label_nivel_jogador_7)
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(40, 340, 160, 41))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_nome_jogador_6 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.label_nome_jogador_6.setObjectName("label_nome_jogador_6")
        self.verticalLayout_15.addWidget(self.label_nome_jogador_6)
        self.label_nivel_jogador_6 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.label_nivel_jogador_6.setObjectName("label_nivel_jogador_6")
        self.verticalLayout_15.addWidget(self.label_nivel_jogador_6)
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(360, 300, 160, 41))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_nome_jogador_12 = QtWidgets.QLabel(self.verticalLayoutWidget_16)
        self.label_nome_jogador_12.setObjectName("label_nome_jogador_12")
        self.verticalLayout_16.addWidget(self.label_nome_jogador_12)
        self.label_nivel_jogador_12 = QtWidgets.QLabel(self.verticalLayoutWidget_16)
        self.label_nivel_jogador_12.setObjectName("label_nivel_jogador_12")
        self.verticalLayout_16.addWidget(self.label_nivel_jogador_12)
        self.verticalLayoutWidget_17 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_17.setGeometry(QtCore.QRect(360, 380, 160, 41))
        self.verticalLayoutWidget_17.setObjectName("verticalLayoutWidget_17")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_17)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_nome_jogador_14 = QtWidgets.QLabel(self.verticalLayoutWidget_17)
        self.label_nome_jogador_14.setObjectName("label_nome_jogador_14")
        self.verticalLayout_17.addWidget(self.label_nome_jogador_14)
        self.label_nivel_jogador_14 = QtWidgets.QLabel(self.verticalLayoutWidget_17)
        self.label_nivel_jogador_14.setObjectName("label_nivel_jogador_14")
        self.verticalLayout_17.addWidget(self.label_nivel_jogador_14)
        self.verticalLayoutWidget_18 = QtWidgets.QWidget(Tela_Guilda)
        self.verticalLayoutWidget_18.setGeometry(QtCore.QRect(360, 340, 160, 41))
        self.verticalLayoutWidget_18.setObjectName("verticalLayoutWidget_18")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_18)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_nome_jogador_13 = QtWidgets.QLabel(self.verticalLayoutWidget_18)
        self.label_nome_jogador_13.setObjectName("label_nome_jogador_13")
        self.verticalLayout_18.addWidget(self.label_nome_jogador_13)
        self.label_nivel_jogador_13 = QtWidgets.QLabel(self.verticalLayoutWidget_18)
        self.label_nivel_jogador_13.setObjectName("label_nivel_jogador_13")
        self.verticalLayout_18.addWidget(self.label_nivel_jogador_13)
        self.botao_sair_guilda = QtWidgets.QPushButton(Tela_Guilda)
        self.botao_sair_guilda.setGeometry(QtCore.QRect(40, 440, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botao_sair_guilda.setFont(font)
        self.botao_sair_guilda.setObjectName("botao_sair_guilda")
        self.botao_retorna_lugar = QtWidgets.QPushButton(Tela_Guilda)
        self.botao_retorna_lugar.setGeometry(QtCore.QRect(580, 0, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_retorna_lugar.setFont(font)
        self.botao_retorna_lugar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_retorna_lugar.setObjectName("botao_retorna_lugar")
        self.botao_deletar_guilda = QtWidgets.QPushButton(Tela_Guilda)
        self.botao_deletar_guilda.setGeometry(QtCore.QRect(360, 440, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botao_deletar_guilda.setFont(font)
        self.botao_deletar_guilda.setObjectName("botao_deletar_guilda")

        self.retranslateUi(Tela_Guilda)
        QtCore.QMetaObject.connectSlotsByName(Tela_Guilda)

    def retranslateUi(self, Tela_Guilda):
        _translate = QtCore.QCoreApplication.translate
        Tela_Guilda.setWindowTitle(_translate("Tela_Guilda", "Form"))
        self.label_nome.setText(_translate("Tela_Guilda", "Guilda:"))
        self.label_nome_jogador_1.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_1.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_integrantes.setText(_translate("Tela_Guilda", "Integrantes"))
        self.label_nome_jogador_2.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_2.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_4.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_4.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_3.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_3.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_9.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_9.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_11.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_11.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_10.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_10.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_8.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_8.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_5.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_5.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_7.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_7.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_6.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_6.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_12.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_12.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_14.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_14.setText(_translate("Tela_Guilda", "Nível:"))
        self.label_nome_jogador_13.setText(_translate("Tela_Guilda", "Nome:"))
        self.label_nivel_jogador_13.setText(_translate("Tela_Guilda", "Nível:"))
        self.botao_sair_guilda.setText(_translate("Tela_Guilda", "Sair da Guilda"))
        self.botao_retorna_lugar.setText(_translate("Tela_Guilda", "X"))
        self.botao_deletar_guilda.setText(_translate("Tela_Guilda", "Deletar Guilda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Guilda = QtWidgets.QWidget()
    ui = Ui_Tela_Guilda()
    ui.setupUi(Tela_Guilda)
    Tela_Guilda.show()
    sys.exit(app.exec_())
