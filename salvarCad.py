from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QRadioButton #do modulo qt widgets importamos aplicações
from PyQt6.QtGui import *
from interfaceCad import  *
import json 

dict_prod = {"Código:" : LineEdit_Cod.text(),
              "Descrição do produto:" : LineEdit_Desc.text(),
              "Preço do produto:" : LineEdit_Prec.text(),
              "Quantidade:" : LineEdit_Quant.text(),}

for k,v in dict_prod.items():
    print (k,v)

object_json = json.dumps(dict_prod, indent=4)

with open('dados.json', 'w',) as arquivo:
    arquivo.write(object_json)

with open('dados.json', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
