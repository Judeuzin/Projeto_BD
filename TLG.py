# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Lista_Guilda.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lista_Guilda(object):
    def setupUi(self, Lista_Guilda):
        Lista_Guilda.setObjectName("Lista_Guilda")
        Lista_Guilda.resize(650, 500)
        self.botao_criar_guilda = QtWidgets.QPushButton(Lista_Guilda)
        self.botao_criar_guilda.setGeometry(QtCore.QRect(30, 440, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botao_criar_guilda.setFont(font)
        self.botao_criar_guilda.setObjectName("botao_criar_guilda")
        self.botao_retorna_lugar = QtWidgets.QPushButton(Lista_Guilda)
        self.botao_retorna_lugar.setGeometry(QtCore.QRect(580, 0, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_retorna_lugar.setFont(font)
        self.botao_retorna_lugar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_retorna_lugar.setObjectName("botao_retorna_lugar")
        self.label_nome = QtWidgets.QLabel(Lista_Guilda)
        self.label_nome.setGeometry(QtCore.QRect(30, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_nome.setFont(font)
        self.label_nome.setObjectName("label_nome")
        self.gridLayoutWidget = QtWidgets.QWidget(Lista_Guilda)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 90, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome_guilda_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_nome_guilda_1.setMinimumSize(QtCore.QSize(130, 0))
        self.label_nome_guilda_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_nome_guilda_1.setObjectName("label_nome_guilda_1")
        self.gridLayout.addWidget(self.label_nome_guilda_1, 0, 0, 1, 1)
        self.label_lider_guilda_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_lider_guilda_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_lider_guilda_1.setObjectName("label_lider_guilda_1")
        self.gridLayout.addWidget(self.label_lider_guilda_1, 1, 0, 1, 1)
        self.botao_seleciona_guilda_1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.botao_seleciona_guilda_1.setText("")
        self.botao_seleciona_guilda_1.setObjectName("botao_seleciona_guilda_1")
        self.gridLayout.addWidget(self.botao_seleciona_guilda_1, 0, 1, 2, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Lista_Guilda)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 170, 160, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_nome_guilda_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_nome_guilda_3.setMinimumSize(QtCore.QSize(130, 0))
        self.label_nome_guilda_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_nome_guilda_3.setObjectName("label_nome_guilda_3")
        self.gridLayout_2.addWidget(self.label_nome_guilda_3, 0, 0, 1, 1)
        self.label_lider_guilda_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_lider_guilda_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_lider_guilda_3.setObjectName("label_lider_guilda_3")
        self.gridLayout_2.addWidget(self.label_lider_guilda_3, 1, 0, 1, 1)
        self.botao_seleciona_guilda_3 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.botao_seleciona_guilda_3.setText("")
        self.botao_seleciona_guilda_3.setObjectName("botao_seleciona_guilda_3")
        self.gridLayout_2.addWidget(self.botao_seleciona_guilda_3, 0, 1, 2, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(Lista_Guilda)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(350, 170, 160, 80))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_nome_guilda_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_nome_guilda_4.setMinimumSize(QtCore.QSize(130, 0))
        self.label_nome_guilda_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_nome_guilda_4.setObjectName("label_nome_guilda_4")
        self.gridLayout_5.addWidget(self.label_nome_guilda_4, 0, 0, 1, 1)
        self.label_lider_guilda_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_lider_guilda_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_lider_guilda_4.setObjectName("label_lider_guilda_4")
        self.gridLayout_5.addWidget(self.label_lider_guilda_4, 1, 0, 1, 1)
        self.botao_seleciona_guilda_4 = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.botao_seleciona_guilda_4.setText("")
        self.botao_seleciona_guilda_4.setObjectName("botao_seleciona_guilda_4")
        self.gridLayout_5.addWidget(self.botao_seleciona_guilda_4, 0, 1, 2, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(Lista_Guilda)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(350, 90, 160, 80))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_nome_guilda_2 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_nome_guilda_2.setMinimumSize(QtCore.QSize(130, 0))
        self.label_nome_guilda_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_nome_guilda_2.setObjectName("label_nome_guilda_2")
        self.gridLayout_6.addWidget(self.label_nome_guilda_2, 0, 0, 1, 1)
        self.label_lider_guilda_2 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_lider_guilda_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_lider_guilda_2.setObjectName("label_lider_guilda_2")
        self.gridLayout_6.addWidget(self.label_lider_guilda_2, 1, 0, 1, 1)
        self.botao_seleciona_guilda_2 = QtWidgets.QRadioButton(self.gridLayoutWidget_6)
        self.botao_seleciona_guilda_2.setText("")
        self.botao_seleciona_guilda_2.setObjectName("botao_seleciona_guilda_2")
        self.gridLayout_6.addWidget(self.botao_seleciona_guilda_2, 0, 1, 2, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(Lista_Guilda)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(350, 250, 160, 80))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_nome_guilda_6 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_nome_guilda_6.setMinimumSize(QtCore.QSize(130, 0))
        self.label_nome_guilda_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_nome_guilda_6.setObjectName("label_nome_guilda_6")
        self.gridLayout_7.addWidget(self.label_nome_guilda_6, 0, 0, 1, 1)
        self.label_lider_guilda_6 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_lider_guilda_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_lider_guilda_6.setObjectName("label_lider_guilda_6")
        self.gridLayout_7.addWidget(self.label_lider_guilda_6, 1, 0, 1, 1)
        self.botao_seleciona_guilda_6 = QtWidgets.QRadioButton(self.gridLayoutWidget_7)
        self.botao_seleciona_guilda_6.setText("")
        self.botao_seleciona_guilda_6.setObjectName("botao_seleciona_guilda_6")
        self.gridLayout_7.addWidget(self.botao_seleciona_guilda_6, 0, 1, 2, 1)
        self.gridLayoutWidget_9 = QtWidgets.QWidget(Lista_Guilda)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(30, 330, 160, 80))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_nome_guilda_7 = QtWidgets.QLabel(self.gridLayoutWidget_9)
        self.label_nome_guilda_7.setMinimumSize(QtCore.QSize(130, 0))
        self.label_nome_guilda_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_nome_guilda_7.setObjectName("label_nome_guilda_7")
        self.gridLayout_9.addWidget(self.label_nome_guilda_7, 0, 0, 1, 1)
        self.label_lider_guilda_7 = QtWidgets.QLabel(self.gridLayoutWidget_9)
        self.label_lider_guilda_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_lider_guilda_7.setObjectName("label_lider_guilda_7")
        self.gridLayout_9.addWidget(self.label_lider_guilda_7, 1, 0, 1, 1)
        self.botao_seleciona_guilda_7 = QtWidgets.QRadioButton(self.gridLayoutWidget_9)
        self.botao_seleciona_guilda_7.setText("")
        self.botao_seleciona_guilda_7.setObjectName("botao_seleciona_guilda_7")
        self.gridLayout_9.addWidget(self.botao_seleciona_guilda_7, 0, 1, 2, 1)
        self.gridLayoutWidget_11 = QtWidgets.QWidget(Lista_Guilda)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(30, 250, 160, 80))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_nome_guilda_5 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_nome_guilda_5.setMinimumSize(QtCore.QSize(130, 0))
        self.label_nome_guilda_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_nome_guilda_5.setObjectName("label_nome_guilda_5")
        self.gridLayout_11.addWidget(self.label_nome_guilda_5, 0, 0, 1, 1)
        self.label_lider_guilda_5 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_lider_guilda_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_lider_guilda_5.setObjectName("label_lider_guilda_5")
        self.gridLayout_11.addWidget(self.label_lider_guilda_5, 1, 0, 1, 1)
        self.botao_seleciona_guilda_5 = QtWidgets.QRadioButton(self.gridLayoutWidget_11)
        self.botao_seleciona_guilda_5.setText("")
        self.botao_seleciona_guilda_5.setObjectName("botao_seleciona_guilda_5")
        self.gridLayout_11.addWidget(self.botao_seleciona_guilda_5, 0, 1, 2, 1)
        self.gridLayoutWidget_12 = QtWidgets.QWidget(Lista_Guilda)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(350, 330, 160, 80))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_nome_guilda_8 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_nome_guilda_8.setMinimumSize(QtCore.QSize(130, 0))
        self.label_nome_guilda_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_nome_guilda_8.setObjectName("label_nome_guilda_8")
        self.gridLayout_12.addWidget(self.label_nome_guilda_8, 0, 0, 1, 1)
        self.label_lider_guilda_8 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_lider_guilda_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_lider_guilda_8.setObjectName("label_lider_guilda_8")
        self.gridLayout_12.addWidget(self.label_lider_guilda_8, 1, 0, 1, 1)
        self.botao_seleciona_guilda_8 = QtWidgets.QRadioButton(self.gridLayoutWidget_12)
        self.botao_seleciona_guilda_8.setText("")
        self.botao_seleciona_guilda_8.setObjectName("botao_seleciona_guilda_8")
        self.gridLayout_12.addWidget(self.botao_seleciona_guilda_8, 0, 1, 2, 1)
        self.botao_entrar_guilda = QtWidgets.QPushButton(Lista_Guilda)
        self.botao_entrar_guilda.setGeometry(QtCore.QRect(479, 440, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botao_entrar_guilda.setFont(font)
        self.botao_entrar_guilda.setObjectName("botao_entrar_guilda")

        self.retranslateUi(Lista_Guilda)
        QtCore.QMetaObject.connectSlotsByName(Lista_Guilda)

    def retranslateUi(self, Lista_Guilda):
        _translate = QtCore.QCoreApplication.translate
        Lista_Guilda.setWindowTitle(_translate("Lista_Guilda", "Form"))
        self.botao_criar_guilda.setText(_translate("Lista_Guilda", "Criar Guilda"))
        self.botao_retorna_lugar.setText(_translate("Lista_Guilda", "X"))
        self.label_nome.setText(_translate("Lista_Guilda", "Lista de Guildas"))
        self.label_nome_guilda_1.setText(_translate("Lista_Guilda", "Nome:"))
        self.label_lider_guilda_1.setText(_translate("Lista_Guilda", "Líder:"))
        self.label_nome_guilda_3.setText(_translate("Lista_Guilda", "Nome:"))
        self.label_lider_guilda_3.setText(_translate("Lista_Guilda", "Líder:"))
        self.label_nome_guilda_4.setText(_translate("Lista_Guilda", "Nome:"))
        self.label_lider_guilda_4.setText(_translate("Lista_Guilda", "Líder:"))
        self.label_nome_guilda_2.setText(_translate("Lista_Guilda", "Nome:"))
        self.label_lider_guilda_2.setText(_translate("Lista_Guilda", "Líder:"))
        self.label_nome_guilda_6.setText(_translate("Lista_Guilda", "Nome:"))
        self.label_lider_guilda_6.setText(_translate("Lista_Guilda", "Líder:"))
        self.label_nome_guilda_7.setText(_translate("Lista_Guilda", "Nome:"))
        self.label_lider_guilda_7.setText(_translate("Lista_Guilda", "Líder:"))
        self.label_nome_guilda_5.setText(_translate("Lista_Guilda", "Nome:"))
        self.label_lider_guilda_5.setText(_translate("Lista_Guilda", "Líder:"))
        self.label_nome_guilda_8.setText(_translate("Lista_Guilda", "Nome:"))
        self.label_lider_guilda_8.setText(_translate("Lista_Guilda", "Líder:"))
        self.botao_entrar_guilda.setText(_translate("Lista_Guilda", "Entrar na Guilda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lista_Guilda = QtWidgets.QWidget()
    ui = Ui_Lista_Guilda()
    ui.setupUi(Lista_Guilda)
    Lista_Guilda.show()
    sys.exit(app.exec_())
