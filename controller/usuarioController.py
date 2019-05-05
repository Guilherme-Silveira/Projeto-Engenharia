from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/logar', methods=['POST'])
def logar():
    # user = request.form.get('email')
    # passwd = request.form.get('senha')
    #valor = user_login(user, passwd) verifica se o usuario existe 
    # if len(valor) > 0:
    #     return redirect('menu')
    # else:
    #     return redirect('/')
    pass

@app.route('/cadastro', methods=['POST'])
def controllerCadastroUsuario():
    # nome = request.form.get('nome')
    # cpf = request.form.get('cpf')
    # rg = request.form.get('rg')
    # email = request.form.get('email')
    # senha = request.form.get('senha')
    print('Entrou no metodo')