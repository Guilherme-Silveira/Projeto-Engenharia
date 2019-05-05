 #Definição da classe usuário
import mysql.connector

from flask import redirect

def novaConexao(self):
        return mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='DB_LOCALIZA', auth_plugin='mysql_native_password')

class Usuario:

    def __init__(self, nome, email, senha, cpf, rg, telefone, tipo, status):

        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.tipo = tipo
        self.status = status

    def teste(self, nome):
        self.nome = nome

    #VALIDAÇÃO DO NOVO USUARIO 
    def validaDadosUsuario(self, usuario):

        if(len(usuario.nome) == 0 or len(usuario.email) == 0):
            return False
        elif(len(usuario.senha) < 3):
            return False
        else:
            return usuario.cadastraUsuario(usuario)

    #CADASTRO EFETIVO 
    def cadastraUsuario(self, novoUsuario):
        conexao = novaConexao(self)
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO USUARIO (CPF_USUARIO, NOME_USUARIO, RG_USUARIO, EMAIL_USUARIO, SENHA_USUARIO, STATUS_USUARIO, ID_TIPO_CONTA) VALUES ('{novoUsuario.cpf}', '{novoUsuario.nome}', '{novoUsuario.rg}', '{novoUsuario.email}', '{novoUsuario.senha}', '{novoUsuario.status}', '{novoUsuario.tipo}')")
        conexao.commit()
        return redirect('/')
        
        
    def consultaUsuario(self, email, senha):
        conexao = novaConexao(self)
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM VW_SELECIONA_USUARIO WHERE EMAIL_USUARIO = '{email}' AND SENHA_USUARIO = '{senha}'")
        user = cursor.fetchall()
        print(user)
        
