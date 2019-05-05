from flask import Flask, render_template, request, url_for, redirect
from model import usuarioModel


app = Flask(__name__)

#PAGINA INICIAL 
@app.route('/')
def index():
    return render_template('login.html')
    

#PAGINA DE CADASTRO DO USUARIO COMUM
@app.route('/cadastro')
def paginaCadastroUsuario():
    return render_template('cadastro.html')

''' 
    Rota para cadastro de usuário comum
    Neste caso será sempre marcado para o tipo comum de usuário, último parâmetro do objeto Usuario

'''
# NA VERDADE ISSO FAZ PARTE DO CONTROLLER DO USUARIO
@app.route('/cadastro', methods=['POST'])
def controllerCadastroUsuario():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    cpf = request.form.get('cpf')
    telefone = request.form.get('telefone')
    tipo = request.form.get('tipo')
    rg = request.form.get('rg')
    
    NovoUsuario = usuarioModel.Usuario(nome, email, senha, cpf, rg, telefone, tipo, 1)
    return NovoUsuario.validaDadosUsuario(NovoUsuario)
    
#------------------------------------------------------

#REALIZA LOGIN 
'''
    Rota para o sistema validar se o tipo de login é Comum ou Administrador

    Deve pegar o e-mail e senha informado pela interface e localizar se existe na base de dados. 

'''
@app.route('/login', methods=['POST'])
def loginUsuario():
    email = request.form.get('email')
    senha = request.form.get('senha')

    usuario = usuarioModel.Usuario.teste(email)
    return email + senha 


## INICIA A APLICAÇÃO 
if __name__ == '__main__':
    app.run(debug=True)