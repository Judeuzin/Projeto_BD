# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Atacar_Monstro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Atq_Monst(object):
    def setupUi(self, Tela_Atq_Monst):
        Tela_Atq_Monst.setObjectName("Tela_Atq_Monst")
        Tela_Atq_Monst.resize(650, 500)
        self.botao_retorna_lugar = QtWidgets.QPushButton(Tela_Atq_Monst)
        self.botao_retorna_lugar.setGeometry(QtCore.QRect(580, 0, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_retorna_lugar.setFont(font)
        self.botao_retorna_lugar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_retorna_lugar.setObjectName("botao_retorna_lugar")
        self.label_nivel = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_nivel.setGeometry(QtCore.QRect(150, 10, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nivel.setFont(font)
        self.label_nivel.setObjectName("label_nivel")
        self.label_nome_monstro = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_nome_monstro.setGeometry(QtCore.QRect(20, 70, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_nome_monstro.setFont(font)
        self.label_nome_monstro.setObjectName("label_nome_monstro")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(Tela_Atq_Monst)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(500, 340, 151, 161))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_nome_proximo_drop = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nome_proximo_drop.sizePolicy().hasHeightForWidth())
        self.label_nome_proximo_drop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_nome_proximo_drop.setFont(font)
        self.label_nome_proximo_drop.setMouseTracking(True)
        self.label_nome_proximo_drop.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_nome_proximo_drop.setObjectName("label_nome_proximo_drop")
        self.verticalLayout_5.addWidget(self.label_nome_proximo_drop)
        self.label_nivel_proximo_drop = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_nivel_proximo_drop.setFont(font)
        self.label_nivel_proximo_drop.setObjectName("label_nivel_proximo_drop")
        self.verticalLayout_5.addWidget(self.label_nivel_proximo_drop)
        self.label_atk_proximo_drop = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_atk_proximo_drop.setFont(font)
        self.label_atk_proximo_drop.setObjectName("label_atk_proximo_drop")
        self.verticalLayout_5.addWidget(self.label_atk_proximo_drop)
        self.label_def_proximo_drop = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_def_proximo_drop.setFont(font)
        self.label_def_proximo_drop.setObjectName("label_def_proximo_drop")
        self.verticalLayout_5.addWidget(self.label_def_proximo_drop)
        self.label_proximo_drop = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_proximo_drop.setGeometry(QtCore.QRect(500, 320, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_proximo_drop.setFont(font)
        self.label_proximo_drop.setObjectName("label_proximo_drop")
        self.botao_atacar = QtWidgets.QPushButton(Tela_Atq_Monst)
        self.botao_atacar.setGeometry(QtCore.QRect(230, 190, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_atacar.setFont(font)
        self.botao_atacar.setObjectName("botao_atacar")
        self.label_vitoria = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_vitoria.setGeometry(QtCore.QRect(280, 140, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_vitoria.setFont(font)
        self.label_vitoria.setObjectName("label_vitoria")
        self.label_derrota = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_derrota.setGeometry(QtCore.QRect(270, 300, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_derrota.setFont(font)
        self.label_derrota.setObjectName("label_derrota")
        self.label_nome_jogador = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_nome_jogador.setGeometry(QtCore.QRect(20, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_nome_jogador.setFont(font)
        self.label_nome_jogador.setObjectName("label_nome_jogador")
        self.label_nivel_jogador = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_nivel_jogador.setGeometry(QtCore.QRect(160, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nivel_jogador.setFont(font)
        self.label_nivel_jogador.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nivel_jogador.setObjectName("label_nivel_jogador")
        self.label_nivel_monstro = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_nivel_monstro.setGeometry(QtCore.QRect(160, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nivel_monstro.setFont(font)
        self.label_nivel_monstro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nivel_monstro.setObjectName("label_nivel_monstro")
        self.label_atk_jogador = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_atk_jogador.setGeometry(QtCore.QRect(240, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_atk_jogador.setFont(font)
        self.label_atk_jogador.setAlignment(QtCore.Qt.AlignCenter)
        self.label_atk_jogador.setObjectName("label_atk_jogador")
        self.label_atk = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_atk.setGeometry(QtCore.QRect(220, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_atk.setFont(font)
        self.label_atk.setObjectName("label_atk")
        self.label_atk_monstro = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_atk_monstro.setGeometry(QtCore.QRect(240, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_atk_monstro.setFont(font)
        self.label_atk_monstro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_atk_monstro.setObjectName("label_atk_monstro")
        self.label_def_jogador = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_def_jogador.setGeometry(QtCore.QRect(320, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_def_jogador.setFont(font)
        self.label_def_jogador.setAlignment(QtCore.Qt.AlignCenter)
        self.label_def_jogador.setObjectName("label_def_jogador")
        self.label_def = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_def.setGeometry(QtCore.QRect(300, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_def.setFont(font)
        self.label_def.setObjectName("label_def")
        self.label_def_monstro = QtWidgets.QLabel(Tela_Atq_Monst)
        self.label_def_monstro.setGeometry(QtCore.QRect(320, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_def_monstro.setFont(font)
        self.label_def_monstro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_def_monstro.setObjectName("label_def_monstro")

        self.retranslateUi(Tela_Atq_Monst)
        QtCore.QMetaObject.connectSlotsByName(Tela_Atq_Monst)

    def retranslateUi(self, Tela_Atq_Monst):
        _translate = QtCore.QCoreApplication.translate
        Tela_Atq_Monst.setWindowTitle(_translate("Tela_Atq_Monst", "Form"))
        self.botao_retorna_lugar.setText(_translate("Tela_Atq_Monst", "X"))
        self.label_nivel.setText(_translate("Tela_Atq_Monst", "Nível"))
        self.label_nome_monstro.setText(_translate("Tela_Atq_Monst", "Monstro"))
        self.label_nome_proximo_drop.setText(_translate("Tela_Atq_Monst", "Nome:"))
        self.label_nivel_proximo_drop.setText(_translate("Tela_Atq_Monst", "Nível:"))
        self.label_atk_proximo_drop.setText(_translate("Tela_Atq_Monst", "Ataque:"))
        self.label_def_proximo_drop.setText(_translate("Tela_Atq_Monst", "Defesa:"))
        self.label_proximo_drop.setText(_translate("Tela_Atq_Monst", "Próximo Drop"))
        self.botao_atacar.setText(_translate("Tela_Atq_Monst", "Atacar"))
        self.label_vitoria.setText(_translate("Tela_Atq_Monst", "Vitória"))
        self.label_derrota.setText(_translate("Tela_Atq_Monst", "Derrota"))
        self.label_nome_jogador.setText(_translate("Tela_Atq_Monst", "Jogador"))
        self.label_nivel_jogador.setText(_translate("Tela_Atq_Monst", "1"))
        self.label_nivel_monstro.setText(_translate("Tela_Atq_Monst", "2"))
        self.label_atk_jogador.setText(_translate("Tela_Atq_Monst", "5"))
        self.label_atk.setText(_translate("Tela_Atq_Monst", "Ataque"))
        self.label_atk_monstro.setText(_translate("Tela_Atq_Monst", "6"))
        self.label_def_jogador.setText(_translate("Tela_Atq_Monst", "4"))
        self.label_def.setText(_translate("Tela_Atq_Monst", "Defesa"))
        self.label_def_monstro.setText(_translate("Tela_Atq_Monst", "7"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Atq_Monst = QtWidgets.QWidget()
    ui = Ui_Tela_Atq_Monst()
    ui.setupUi(Tela_Atq_Monst)
    Tela_Atq_Monst.show()
    sys.exit(app.exec_())
