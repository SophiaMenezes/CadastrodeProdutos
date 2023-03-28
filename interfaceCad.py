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

     if bot1.isChecked():
          print('Categoria: Alimentos')
     elif bot2.isChecked():
          print('Categoria: Eletrodomésticos')
     else:
          print('Categoria: Eletrônicos \n')

def chamarListaProdutos():
     interfaceList.show()

cadastro = QLabel("Cadastro de Novo Produto", interfaceCad)
cadastro.move(100,150) #eixo x, eixo y, largura e altura
cadastro.setStyleSheet('font-size:15px')

categoria = QLabel("Categoria", interfaceCad)
categoria.move(100,360)
categoria.setStyleSheet('font-size:15px')

bot1 = QRadioButton("Alimentos",interfaceCad)
bot1.setGeometry(200,360,150,20)
bot2 = QRadioButton("Eletrodomésticos", interfaceCad)
bot2.setGeometry(200,380,150,20)
bot3 = QRadioButton("Eletrônicos", interfaceCad)
bot3.setGeometry(200,400,150,20)

LineEdit_Cod = QLineEdit("Código do Produto: ", interfaceCad)
LineEdit_Cod.setGeometry(300,150,300,40)
LineEdit_Desc = QLineEdit("Descrição: ", interfaceCad)
LineEdit_Desc.setGeometry(300,200,300,40)
LineEdit_Prec = QLineEdit("Preço por Unidade: ", interfaceCad)
LineEdit_Prec.setGeometry(300,250,300,40)
LineEdit_Quant = QLineEdit("Quantidade: ", interfaceCad)
LineEdit_Quant.setGeometry(300,300,300,40)

envio = QPushButton("Salvar", interfaceCad)
envio.setGeometry(450, 500, 100, 50)
envio.clicked.connect(função_principal)

lista = QPushButton("Listar Produtos", interfaceCad)
lista.setGeometry(250, 500, 100, 50)
lista.clicked.connect(chamarListaProdutos)

label = QLabel("Cadastro de Produtos", interfaceCad)
label.move(300,45) #larg, alt
label.setStyleSheet('font-size:20px')

interfaceCad.show() #mostrar tela

app.exec()
