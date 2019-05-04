from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/logar', methods=['POST'])
def logar():
    user = request.form.get('email')
    passwd = request.form.get('senha')
    #valor = user_login(user, passwd) verifica se o usuario existe 
    if len(valor) > 0:
        return redirect('menu')
    else:
        return redirect('/')