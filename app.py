from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from models.libri import db,Libri
from routes.libri import libri_bp

app = Flask(__name__)

# Configura il percorso del database SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'libri.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza SQLAlchemy
db.init_app(app)

app.register_blueprint(libri_bp,url_prefix= '/api')


    
@app.route('/home')
def form():
    return render_template('form.html')

@app.route('/libri')
def libri():
    return render_template('libri.html')

@app.route('/utenti')
def utenti():
    return render_template('utenti.html')

# Rotta di base per testare il server
@app.route('/')
def home():
    return "Benvenuto nella Libreria API!"


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
app.run(debug=True)