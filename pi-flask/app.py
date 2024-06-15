from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

app.secret_key ='mysecretkey'

mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registros')
def registros():
    return render_template('registros.html')

@app.route('/registros')
def registros():
    return render_template('registros.html')

@app.route('/registros')
def registros():
    return render_template('registros.html')

@app.route('/registros')
def registros():
    return render_template('registros.html')

@app.route('/registros')
def registros():
    return render_template('registros.html')     
     
@app.errorhandler(404)     
def paginando(e):
    return 'Ruta inexistente'
     
if __name__ == '__main__':
    app.run(debug=True, port=8800)