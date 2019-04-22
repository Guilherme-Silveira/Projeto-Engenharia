from math import radians, sin, cos, asin, sqrt, atan, degrees
from geopy.geocoders import GoogleV3
import MySQLdb
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def conexao():
    return MySQLdb.connect(host='localhost', user='mercado', passwd='mercado', db='mydb')

def user_login(u, p):
    cursor = conexao().cursor()
    cursor.execute(f"SELECT * FROM USUARIO WHERE EMAIL_USUARIO='{u}' AND SENHA_USUARIO='{p}'")
    user = cursor.fetchall()
    return user

def tipo_user():
    cursor = conexao().cursor()
    cursor.execute('SELECT DESC_TIPO_CONTA FROM TIPO_CONTA')
    tipos = cursor.fetchall()
    return tipos

def torres():
    cursor = conexao().cursor()
    cursor.execute('SELECT LATIT_TORRE, LOGIT_TORRE FROM TORRE_SITE ')
    torres = cursor.fetchall()
    return torres

def antenas():
    cursor = conexao().cursor()
    cursor.execute('SELECT DESC_ANTENA, AZIMUTE_ANTENA, STATUS_ANTENA FROM ANTENA_SETOR')
    return cursor.fetchall()

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('login.jinja2')

@app.route('/login')
def login():
    tipo = tipo_user()
    return render_template('cadastro.html', tipo_usuario = tipo)


@app.route('/logar', methods=['POST'])
def logar():
    user = request.form.get('email')
    passwd = request.form.get('senha')
    valor = user_login(user, passwd)
    if len(valor) > 0:
        return redirect('menu')
    else:
        return redirect('/')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    con = conexao()
    cursor = con.cursor()
    cpf = request.form.get("cpf")
    nome = request.form.get("nome")
    rg = request.form.get("rg")
    email = request.form.get("email")
    senha = request.form.get("senha")
    tipo = request.form.get("tipo")
    cursor.execute(f"INSERT INTO USUARIO(CPF_USUARIO, NOME_USUARIO, RG_USUARIO, EMAIL_USUARIO, SENHA_USUARIO, STATUS_USUARIO, TIPO_CONTA_ID_TIPO_CONTA) VALUES('{cpf}', '{nome}', '{rg}', '{email}', '{senha}', {True}, {int(tipo)})")
    con.commit()
    return redirect('/')

@app.route('/menu', methods=['POST', 'GET'])
def menu():
    return render_template('home.jinja2')

def areaInside(a, b, c, d):
# Formula de Haversine
    r = 6371

    # Converte coordenadas de graus para radianos
    lat1, lon1, lat2, lon2 = map(radians, [ float(a), float(b), float(c), float(d) ] )

    # Formula de Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    hav = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distancia = 2 * r * asin( sqrt(hav) )
    if distancia <= 1.5:
        return True
    else:
        return False
        
def azi(a, b, c, d):
    # Converte coordenadas de graus para radianos
    lat1, lon1, lat2, lon2 = map(radians, [ float(a), float(b), float(c), float(d) ] )

    # Formula de Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    azimute = atan(dlat/dlon)
    return degrees(azimute)
    
@app.route('/resultado', methods=['POST'])
def resultado():
    geolocator = GoogleV3(api_key='AIzaSyDLxvmCIqDmidp84dgKwXemApra3XtUhUE')
    location = geolocator.geocode(str(request.form.get('exemplo')))
    tower = torres()
    return render_template('resultado.jinja2', location = location, tower = tower, areaInside = areaInside, azimute=azi, antenas=antenas, float = float)
    

if __name__=='__main__':
#    app.run(debug=True)
    geolocator = GoogleV3(api_key='AIzaSyDLxvmCIqDmidp84dgKwXemApra3XtUhUE')
    location = geolocator.geocode('Alameda Vicente Leporace, 4655 - Parque dos Pinhais, Franca - SP, 14405-610')
    tower = torres()
    for j, i in enumerate(tower):
        print(areaInside(location.latitude, location.longitude, i[0], i[1]))
        if areaInside(location.latitude, location.longitude, i[0], i[1]) == True:
            if j==0:
                for k in antenas()[0:3]:
                    azimute = azi(location.latitude, location.longitude, i[0], i[1])
                    if float(azimute)>=k[1]-32.5 and float(azimute)<=k[1]+32.5:
                        print(k[0], True)
            if j==1:
                for k in antenas()[3:6]:
                    azimute = azi(location.latitude, location.longitude, i[0], i[1])
                    if float(azimute)>=k[1]-32.5 and float(azimute)<=k[1]+32.5:
                        print(k[0], True)
            if j==2:
                for k in antenas()[6:9]:
                    azimute = azi(location.latitude, location.longitude, i[0], i[1])
                    if float(azimute)>=k[1]-32.5 and float(azimute)<=k[1]+32.5:
                        print(k[0], True)
            if j==3:
                for k in antenas()[9:12]:
                    azimute = azi(location.latitude, location.longitude, i[0], i[1])
                    if float(azimute)>=k[1]-32.5 and float(azimute)<=k[1]+32.5:
                        print(k[0], True)
        print('---------------------------')