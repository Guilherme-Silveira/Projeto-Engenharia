#Classe de conexão
import mysql.connector

class Conexao:

    def novaConexao(self):
        return mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='DB_LOCALIZA', auth_plugin='mysql_native_password')

