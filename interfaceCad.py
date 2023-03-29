import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QRadioButton #do modulo qt widgets importamos aplicações
from PyQt6.QtGui import *

app = QApplication(sys.argv)

interfaceCad = QWidget()
interfaceCad.resize(800,600) #tam da janela alt/larg
interfaceCad.setWindowTitle("Cadastro de Produtos")

interfaceList = QWidget()
interfaceList.resize(800,600) #tam da janela alt/larg
interfaceList.setWindowTitle("Lista de Produtos")

def função_principal():
     linha1 = LineEdit_Cod.text()
     print(linha1)
     linha2 = LineEdit_Desc.text()
     print(linha2)
     linha3 = LineEdit_Prec.text()
     print(linha3)
     linha4 = LineEdit_Quant.text()
     print(linha4)

def chamarListaProdutos():
     interfaceList.show()

codigo = QLabel("Codigo do produto: ", interfaceCad)
codigo.move(210,153) #eixo x, eixo y, largura e alt
codigo.setStyleSheet('font-size:15px')

descricao = QLabel("Descrição do produto: ", interfaceCad)
descricao.move(194,203) #eixo x, eixo y, largura e alt
descricao.setStyleSheet('font-size:15px')

preco = QLabel("Preço do produto: ", interfaceCad)
preco.move(222,253) #eixo x, eixo y, largura e alt
preco.setStyleSheet('font-size:15px')

quantidade = QLabel("Quantidade: ", interfaceCad)
quantidade.move(261,303) #eixo x, eixo y, largura e alt
quantidade.setStyleSheet('font-size:15px')


LineEdit_Cod = QLineEdit("", interfaceCad)
LineEdit_Cod.setGeometry(350,150,150,30)
LineEdit_Desc = QLineEdit("", interfaceCad)
LineEdit_Desc.setGeometry(350,200,150,30)
LineEdit_Prec = QLineEdit("", interfaceCad)
LineEdit_Prec.setGeometry(350,250,150,30)
LineEdit_Quant = QLineEdit("", interfaceCad)
LineEdit_Quant.setGeometry(350,300,150,30)

envio = QPushButton("Salvar", interfaceCad)
envio.setGeometry(450, 500, 100, 50)
envio.clicked.connect(função_principal)

lista = QPushButton("Listar Produtos", interfaceCad)
lista.setGeometry(250, 500, 100, 50)
lista.clicked.connect(chamarListaProdutos)

label = QLabel("Cadastro de Produtos", interfaceCad)
label.move(250,45) #larg, alt
label.setStyleSheet('font-size:30px')

interfaceCad.show() #mostrar tela

app.exec()
