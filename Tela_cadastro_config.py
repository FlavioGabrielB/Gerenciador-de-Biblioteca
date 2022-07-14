from msilib.schema import Error
import sys
from datetime import date
from traceback import print_tb
from urllib import error 
from beautiful_date import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Tela_cadastro import Ui
from Tela_edicao import *
import sqlite3
import openpyxl
import pandas as pd
import os







class config(QMainWindow, Ui):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.label.setText("Bem-vindo!")
        self.pushButton_5.clicked.connect(self.enviar)
        self.pushButton_2.clicked.connect(self.excluir_msg)
        self.d = '''CREATE TABLE IF NOT EXISTS dados (id integer not null primary key autoincrement, nome_aluno text, ano_serie text, nome_livro text, genero text, dias text, devolver text)'''

        self.banco = sqlite3.connect('banco_cadastro.db')
        self.csr = self.banco.cursor()
        self.csr.execute(self.d)
        self.banco.commit()
        self.banco.close()
        self.pushButton_4.clicked.connect(self.excluir_row)
        self.pushButton_3.clicked.connect(self.editar)
        self.pushButton_6.clicked.connect(self.atualizar)
        self.pushButton_7.clicked.connect(self.excel)

        

        self.atualizar()
        
    def excel(self):
        try:
            self.banco = sqlite3.connect('banco_cadastro.db')
            self.csr = self.banco.cursor()
            self.csr.execute("SELECT * FROM dados")
            self.dados_lidos = self.csr.fetchall()
            self.dados_lidos = pd.DataFrame(self.dados_lidos, columns=['id','nome_aluno', 'ano_serie', 'nome_livro', 'genero', 'dias', 'Dia da devolução'])
            self.dados_lidos.to_excel('Tabela.xlsx')
            self.banco.commit()
            self.banco.close()
            os.system('Tabela.xlsx')
        except:
            self.label.setText("Ocorreu um Erro!")

    def enviar(self):
        self.datadehoje = date.today()
        self.dias = int(self.spinBox.text())
        self.dia_amanha = BeautifulDate(self.datadehoje.year,self.datadehoje.month,self.datadehoje.day)
        self.df = str(self.dia_amanha + self.dias*days)
        self.dff = self.df[8]+self.df[9]+self.df[7]+self.df[5]+self.df[6]+self.df[4]+self.df[0]+self.df[1]+self.df[2]+self.df[3]
        self.nome_aluno = self.lineEdit.text()
        self.nome_livro = self.lineEdit_2.text()
        self.genero = self.comboBox.currentText()
        self.ano_serie = self.comboBox_2.currentText()
        self.b = f'''INSERT INTO dados(nome_aluno, ano_serie, nome_livro, genero, dias, devolver)
                    VALUES('{self.nome_aluno}', '{self.ano_serie}', '{self.nome_livro}', '{self.genero}', '{self.dias}', '{self.dff}')'''
        try:
            self.banco = sqlite3.connect('banco_cadastro.db')
            self.csr = self.banco.cursor()
            self.csr.execute(self.b)
            self.banco.commit()
            self.banco.close()
            print('Cadastrado com Sucesso!')
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.label.setText("Cadastrado com Sucesso!")
        except sqlite3.Error as erro:
            self.label.setText("Ocorreu um Erro!")
            print(erro)
        self.atualizar()

    def excluir_msg(self):
        self.label.setText("")
    
    def atualizar(self):
        self.banco = sqlite3.connect('banco_cadastro.db', timeout=1)
        self.csr = self.banco.cursor()
        self.csr.execute('SELECT id, nome_aluno, ano_serie, nome_livro, genero, dias, devolver  FROM dados')
        self.dados_lidos = self.csr.fetchall()
        self.tableWidget.setRowCount(len(self.dados_lidos))
        self.tableWidget.setColumnCount(7)
        print(self.dados_lidos)
        for self.i in range(0, len(self.dados_lidos)):
            for self.j in range(0,7):
                self.tableWidget.setItem(self.i,self.j,QTableWidgetItem(str(self.dados_lidos[self.i][self.j])))
        self.banco.close()
        
        


        

    def excluir_row(self):
        try:
            self.linha = self.tableWidget.currentRow()
            self.tableWidget.removeRow(self.linha)
            self.banco = sqlite3.connect('banco_cadastro.db')
            self.csr = self.banco.cursor()
            self.csr.execute("SELECT id FROM dados")
            self.dados_lidos = self.csr.fetchall()
            self.valor_id = self.dados_lidos[self.linha][0]
            print(self.valor_id)
            self.csr.execute("DELETE FROM dados WHERE id=" + str(self.valor_id))
            self.banco.commit()
            self.banco.close()
        except:
            self.label.setText("Linha inexistente!")
    
    
    def editar(self):
        try:
            self.linha = self.tableWidget.currentRow()
            self.banco = sqlite3.connect('banco_cadastro.db')
            self.csr = self.banco.cursor()
            self.csr.execute("SELECT id FROM dados")
            self.dados_lidos = self.csr.fetchall()
            self.valor_id = self.dados_lidos[self.linha][0]

            self.csr.execute("SELECT * FROM dados WHERE id=" + str(self.valor_id))
            self.produto = self.csr.fetchall()
            print(self.produto)
            self.banco.commit()
            self.banco.close()
            
            #self.edit2 = editar_m()
            #self.edit3 = edicao()
            self.edit = editar_m(str(self.produto[0][0]), str(self.produto[0][1]), str(self.produto[0][3]))
            print(type(self.edit.idd))
            self.edit.show()
            #editar_m().valor("Teste")
            #self.edit3.lineEdit.setText("TEste")

            #self.edit1.lineEdit.setText(str(self.produto[0][1]))
            #self.edit1.lineEdit_2.setText(str(self.produto[0][3]))
        except:
            self.label.setText("Linha inexistente!")


class editar_m(QMainWindow, edicao):
    def __init__(self, idd, a, b):
        self.a = a
        self.b = b
        self.idd = idd
        self.iddd = int(self.idd)
        print(self.a)
        super(editar_m, self).__init__()
        self.edit = edicao()
        self.edit.setupUi(self)

        self.edit.lineEdit.setText(self.a)
        self.edit.lineEdit_2.setText(self.b)
        self.edit.pushButton_5.clicked.connect(self.editando)
        config().atualizar()

    def editando(self):
        self.nm = self.edit.lineEdit.text()
        self.nl = self.edit.lineEdit_2.text()
        self.ge = self.edit.comboBox.currentText()
        self.sa = self.edit.comboBox_2.currentText()
        self.nu = self.edit.spinBox.text()

        

        self.dh = date.today()
        self.di = int(self.nu)
        self.dia_amanha = BeautifulDate(self.dh.year,self.dh.month,self.dh.day)
        self.df = str(self.dia_amanha + self.di*days)
        self.dfff = self.df[8]+self.df[9]+self.df[7]+self.df[5]+self.df[6]+self.df[4]+self.df[0]+self.df[1]+self.df[2]+self.df[3]
        self.banco = sqlite3.connect('banco_cadastro.db')
        self.csr = self.banco.cursor()
        #self.d = '''UPDATE dados SET nome_aluno = {}, ano_serie = {}, nome_livro = {}, genero = {}, dias = {}, devolver = {}'''
        self.csr.execute(f'''UPDATE dados SET nome_aluno = "{self.nm}", ano_serie = "{self.sa}", nome_livro = "{self.nl}", genero = "{self.ge}", dias = "{self.nu}", devolver = "{self.dfff}" WHERE id = "{self.iddd}"''')
        self.banco.commit()
        self.banco.close()
        self.close()

       
        




if __name__ == '__main__':
    qt = QApplication(sys.argv)
    view = config()
    view.show()
    qt.exec()