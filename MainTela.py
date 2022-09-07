from PyQt5 import QtCore, QtGui, QtWidgets
import MainBD
import sys

class Ui_TelaRegistro(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui_TelaRegistro, self).__init__()
        self.setupUiTelaRegistro()

    def Volta_TelaLogin(self):
        widget.setCurrentWidget(PrimeiraPagina)

    def VerificaRegistro(self):
        param1 = self.textLogin.text()
        param2 = self.textSenha.text()
        cond = MainBD.ChamaCamadaPersistenciaRegistro(param1,param2) 
        if cond:
            widget.setCurrentWidget(PrimeiraPagina)
        else:
            print("Preciso Fazer o Pop-UP")

    def retranslateUi(self, CriarConta):
        _translate = QtCore.QCoreApplication.translate
        CriarConta.setWindowTitle(_translate("CriarConta", "CriarConta"))
        self.EfetuaRegistro.setText(_translate("CriarConta", "Criar Conta"))
        self.label_1.setText(_translate("CriarConta", "Criar Conta"))
        self.label_2.setText(_translate("CriarConta", "User ID"))
        self.label_3.setText(_translate("CriarConta", "Senha"))
        self.VoltaTela.setText(_translate("CriarConta", "Voltar"))

    def setupUiTelaRegistro(self):
        self.setObjectName("CriarConta")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(255, 228, 203);\n"
                            "border-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(310, 160, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_1.setFont(font)
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 270, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 320, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 240, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.textLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.textLogin.setGeometry(QtCore.QRect(300, 280, 231, 31))
        self.textLogin.setObjectName("textLogin")
        self.textSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.textSenha.setGeometry(QtCore.QRect(300, 330, 231, 31))
        self.textSenha.setObjectName("textSenha")
        self.EfetuaRegistro = QtWidgets.QPushButton(self.centralwidget)
        self.EfetuaRegistro.setGeometry(QtCore.QRect(370, 390, 93, 28))
        self.EfetuaRegistro.setObjectName("EfetuaRegistro")
        self.VoltaTela = QtWidgets.QPushButton(self.centralwidget)
        self.VoltaTela.setGeometry(QtCore.QRect(680, 520, 93, 28))
        self.VoltaTela.setObjectName("VoltaTela")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        self.EfetuaRegistro.clicked.connect(self.VerificaRegistro)
        self.VoltaTela.clicked.connect(self.Volta_TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(self)
    
class Ui_TelaLogin(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui_TelaLogin, self).__init__()
        self.setupUiTelaLogin()
    
    def VerificaLogin(self):
        param1 = self.textLogin.text()
        param2 = self.textSenha.text()
        cond = MainBD.ChamaCamadaPersistenciaLogin(param1,param2)
        if cond:
            widget.setCurrentWidget(TerceiraPagina)
        else:
            print("Preciso fazer o Pop-UP")
            
    def Troca_TelaRegistro(self):
        widget.setCurrentWidget(SegundaPagina)

    def retranslateUi(self, TelaInicial):
        _translate = QtCore.QCoreApplication.translate
        TelaInicial.setWindowTitle(_translate("TelaInicial", "Game"))
        self.label_1.setText(_translate("TelaInicial", "Tales of a BD Project"))
        self.FechaJogo.setText(_translate("TelaInicial", "Fechar jogo"))
        self.EfetuaLogin.setText(_translate("TelaInicial", "Entrar"))
        self.label_2.setText(_translate("TelaInicial", "User ID"))
        self.label_3.setText(_translate("TelaInicial", "Senha"))
        self.CriaConta.setText(_translate("TelaInicial", "Criar Conta"))
    
    def setupUiTelaLogin(self):
        self.setObjectName("TelaInicial")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(255, 228, 203);\n"
                            "border-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(200, 120, 401, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_1.setFont(font)
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setObjectName("label_1")
        self.FechaJogo = QtWidgets.QPushButton(self.centralwidget)
        self.FechaJogo.setGeometry(QtCore.QRect(690, 500, 93, 28))
        self.FechaJogo.setObjectName("FechaJogo")
        self.EfetuaLogin = QtWidgets.QPushButton(self.centralwidget)
        self.EfetuaLogin.setGeometry(QtCore.QRect(310, 370, 93, 28))
        self.EfetuaLogin.setObjectName("EfetuaLogin")
        self.textLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.textLogin.setGeometry(QtCore.QRect(300, 260, 231, 31))
        self.textLogin.setObjectName("textLogin")
        self.textSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.textSenha.setGeometry(QtCore.QRect(300, 310, 231, 31))
        self.textSenha.setObjectName("textSenha")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 250, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 300, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 220, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.CriaConta = QtWidgets.QPushButton(self.centralwidget)
        self.CriaConta.setGeometry(QtCore.QRect(430, 370, 93, 28))
        self.CriaConta.setObjectName("CriaConta")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        self.EfetuaLogin.clicked.connect(self.VerificaLogin)
        self.CriaConta.clicked.connect(self.Troca_TelaRegistro)
        self.FechaJogo.clicked.connect(app.closeAllWindows)
        QtCore.QMetaObject.connectSlotsByName(self)

class Ui_TelaServidor(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui_TelaServidor, self).__init__()
        Servidores = MainBD.ChamaCamadaPersistenciaServidor()
        self.setupUiTelaServidor(Servidores)

    def Volta_TelaLogin(self):
        widget.setCurrentWidget(PrimeiraPagina)

    def ServidorEscolhido(self):
        param1 = self.EscolheServidor.currentItem().text()
        # aqui é onde precisamos da camada de persistencia
        print(param1)

    def retranslateUi(self, TelaServidor):
        _translate = QtCore.QCoreApplication.translate
        TelaServidor.setWindowTitle(_translate("EscolheServidor", "EscolheServidor"))
        self.label_1.setText(_translate("EscolheServidor", "Escolha o servidor que deseja entrar :"))
        self.VoltaTela.setText(_translate("EscolheServidor", "Voltar Pagina Inicial"))
        self.EfetuaServidor.setText(_translate("EscolheServidor", "Entrar"))
    def setupUiTelaServidor(self,list):
        self.setObjectName("CriarConta")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(255, 228, 203);\n"
            "border-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(40, 50, 400, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setObjectName("label_1")
        self.EscolheServidor = QtWidgets.QListWidget(self.centralwidget)
        self.EscolheServidor.setGeometry(QtCore.QRect(170, 200, 456, 192))
        self.EscolheServidor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                            "border-color: rgb(0, 0, 0);")
        self.EscolheServidor.setObjectName("EscolheServidor")
        self.EfetuaServidor = QtWidgets.QPushButton(self.centralwidget)
        self.EfetuaServidor.setGeometry(QtCore.QRect(350, 420, 93, 28))
        self.EfetuaServidor.setObjectName("EfetuaServidor")
        cont = 0
        for server in list:
            _translate = QtCore.QCoreApplication.translate
            item = QtWidgets.QListWidgetItem()
            self.EscolheServidor.addItem(item)
            __sortingEnabled = self.EscolheServidor.isSortingEnabled()
            self.EscolheServidor.setSortingEnabled(False)
            item = self.EscolheServidor.item(cont)
            server = str(server)
            server = server[2:len(server)-3]
            item.setText(_translate("Dialog",server))
            self.EscolheServidor.setSortingEnabled(__sortingEnabled)
            cont = cont+1
        self.EscolheServidor.setCurrentItem(item)
        self.VoltaTela = QtWidgets.QPushButton(self.centralwidget)
        self.VoltaTela.setGeometry(QtCore.QRect(580, 520, 150, 28))
        self.VoltaTela.setObjectName("VoltaTela")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        self.VoltaTela.clicked.connect(self.Volta_TelaLogin)
        self.EfetuaServidor.clicked.connect(self.ServidorEscolhido)
        QtCore.QMetaObject.connectSlotsByName(self)

class Ui_TelaPersonagem(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui_TelaPersonagem, self).__init__()
        # mudar aqui essa lista de numeros
        self.setupUiTelaPersonagem([1,2,3,4,5,6])

    def Volta_TelaServidor(self):
        widget.setCurrentWidget(TerceiraPagina)

    def PersonagemEscolhido(self):
        param1 = self.EscolhePersonagem.currentItem().text()
        # aqui é onde precisamos da camada de persistencia
        print(param1)

    def retranslateUi(self, TelaPersonagem):
        _translate = QtCore.QCoreApplication.translate
        TelaPersonagem.setWindowTitle(_translate("EscolhePersonagem", "EscolhePersonagem"))
        self.label_1.setText(_translate("EscolhePersonagem", "Escolha o personagem que deseja jogar :"))
        self.VoltaTela.setText(_translate("EscolhePersonagem", "Voltar Pagina Servidor"))
        self.EfetuaPersonagem.setText(_translate("EscolhePersonagem", "Entrar"))
    
    def setupUiTelaPersonagem(self,list):
        self.setObjectName("CriarConta")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(255, 228, 203);\n"
            "border-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(40, 50, 400, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setObjectName("label_1")
        self.EscolhePersonagem = QtWidgets.QListWidget(self.centralwidget)
        self.EscolhePersonagem.setGeometry(QtCore.QRect(170, 200, 456, 192))
        self.EscolhePersonagem.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                            "border-color: rgb(0, 0, 0);")
        self.EscolhePersonagem.setObjectName("EscolhePersonagem")
        self.EfetuaPersonagem = QtWidgets.QPushButton(self.centralwidget)
        self.EfetuaPersonagem.setGeometry(QtCore.QRect(350, 420, 93, 28))
        self.EfetuaPersonagem.setObjectName("EfetuaPersonagem")
        cont = 0
        for server in list:
            _translate = QtCore.QCoreApplication.translate
            item = QtWidgets.QListWidgetItem()
            self.EscolhePersonagem.addItem(item)
            __sortingEnabled = self.EscolhePersonagem.isSortingEnabled()
            self.EscolhePersonagem.setSortingEnabled(False)
            item = self.EscolhePersonagem.item(cont)
            item.setText(_translate("Dialog",str(server)))
            self.EscolhePersonagem.setSortingEnabled(__sortingEnabled)
            cont = cont+1
        self.EscolhePersonagem.setCurrentItem(item)
        self.VoltaTela = QtWidgets.QPushButton(self.centralwidget)
        self.VoltaTela.setGeometry(QtCore.QRect(580, 520, 150, 28))
        self.VoltaTela.setObjectName("VoltaTela")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi(self)
        self.VoltaTela.clicked.connect(self.Volta_TelaServidor)
        self.EfetuaPersonagem.clicked.connect(self.PersonagemEscolhido)
        QtCore.QMetaObject.connectSlotsByName(self)

MainBD

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedHeight(600)
widget.setFixedWidth(800)
PrimeiraPagina = Ui_TelaLogin()
widget.addWidget(PrimeiraPagina)
SegundaPagina = Ui_TelaRegistro()
widget.addWidget(SegundaPagina)
TerceiraPagina = Ui_TelaServidor()
widget.addWidget(TerceiraPagina)
QuartaPagina = Ui_TelaPersonagem()
widget.addWidget(QuartaPagina)
widget.setCurrentWidget(PrimeiraPagina) 
widget.show()
app.exec_()
