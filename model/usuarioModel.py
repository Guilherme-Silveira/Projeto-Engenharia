 #Definição da classe usuário

from conexao import Conexao

class Usuario:

    def __init__(self, nome, email, senha, cpf, telefone, tipo, status):

        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.telefone = telefone
        self.tipo = tipo
        self.status = status

    
    def validaDadosUsuario(self, usuario):

        if(usuario.nome == '' or usuario.email == ''):
            return False
        elif(len(usuario.senha) < 3):
            return False
        else:
            return True

    def cadastraUsuario(self, novoUsuario):
        
        if(self.validaDadosUsuario(novoUsuario)):
            print('Usuario válido para cadastro!')
        else:
            print('Usuario não válido para cadastro')


    def consultaUsuario(self, email, senha):
        conexao = Conexao().novaConexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT ID_USUARIO, CPF_USUARIO ,NOME_USUARIO ,EMAIL_USUARIO ,SENHA_USUARIO ,STATUS_USUARIO ,TC.DESC_TIPO_CONTA FROM USUARIO U INNER JOIN TIPO_CONTA TC ON (U.ID_TIPO_CONTA = TC.ID_TIPO_CONTA) WHERE U.EMAIL_USUARIO = '{email}' AND U.SENHA_USUARIO = '{senha}'")
        user = cursor.fetchall()
        print(user)
        
