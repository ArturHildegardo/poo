import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication
from tela_inicial import Tela_inicial
from tela_busca import Tela_busca
from tela_cadastro import Tela_cadastro
from pessoa import Pessoa
from cadastro import Cadastro

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)
        
        self.tela_busca = Tela_busca()
        self.tela_busca.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
    
class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.tela_inicial.pushButtonMainCadastrar.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButtonMainBuscar.clicked.connect(self.abrirTelaBusca)

        self.tela_cadastro.pushButtonCadastroCadastrar.clicked.connect(self.botaoCadastra)
        self.tela_busca.pushButtonBuscaBuscar.clicked.connect(self.botaoBusca)

        self.tela_busca.pushButtonBuscaVoltar.clicked.connect(self.abrirMenu)
    def botaoCadastra(self):
        nome = self.tela_cadastro.lineEditCadastroNome.text()
        endereco = self.tela_cadastro.lineEditCadastroEndereco.text()
        cpf = self.tela_cadastro.lineEditCadastroCpf.text()
        nascimento = self.tela_cadastro.lineEditCadastroNascimento.text()
        if not(nome == "" or endereco == "" or cpf == "" or nascimento == ""):
            p = Pessoa(nome,endereco,cpf,nascimento)
            if(self.cad.cadastra(p)):
                QMessageBox.information(None,"POOII","Cadastro Realizado Com Sucesso!")
                self.tela_cadastro.lineEditCadastroNome.setText("")
                self.tela_cadastro.lineEditCadastroEndereco.setText("")
                self.tela_cadastro.lineEditCadastroCpf.setText("")
                self.tela_cadastro.lineEditCadastroNascimento.setText("")
            else:
                QMessageBox.information(None,"POOII","Cpf não encontrado!")
        else:
            QMessageBox.information(None,"POOII","Todos os Valores Devem Ser Preenchidos")
        self.QtStack.setCurrentIndex(0)

    def botaoBusca(self):
        cpf = self.tela_busca.lineEditBuscaCpf.text()
        if cpf != "":
            pessoa = self.cad.busca(cpf)
            if pessoa is not None:
                self.tela_busca.lineEditBuscaNome.setText(pessoa.nome)
                self.tela_busca.lineEditBuscaEndereco.setText(pessoa.endereco)
                self.tela_busca.lineEdit_4.setText(pessoa.nascimento)
            else:
                QMessageBox.information(None,"POOII", "Cpf nao encontrado!")
        else:
            QMessageBox.information(None,"POOII", "Preencha o Cpf")

    def abrirMenu(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBusca(self):
        self.QtStack.setCurrentIndex(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

