from flask import Flask, render_template
import os
from models.models import db
from routes.libri import libri_bp
from routes.categorie import categorie_bp
from services.autori_service import get_all_autori
from services.categorie_service import get_all_categorie

app = Flask(__name__)

# Configura il percorso del database SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'libri.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza SQLAlchemy
db.init_app(app)

app.register_blueprint(libri_bp,url_prefix= '/api')
app.register_blueprint(categorie_bp,url_prefix= '/api')


    
@app.route('/home')
def form():
    return render_template('form.html')

@app.route('/libri')
def libri():
    autori = get_all_autori()
    categorie = get_all_categorie()
    return render_template('libri.html', autori=autori,categorie = categorie)

@app.route('/utenti')
def utenti():
    return render_template('utenti.html')

@app.route('/cerca')
def cerca():
    return render_template('cerca.html')

@app.route('/categorie')
def categorie():
    categorie = get_all_categorie()
    return render_template('categorie.html', categorie=categorie)

# Rotta di base per testare il server
@app.route('/')
def home():
    return "Benvenuto nella Libreria API!"


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
app.run(debug=True)