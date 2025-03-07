from functools import wraps
from flask import Flask, render_template, abort
import os
from models.models import db,Utente
from routes.libri import libri_bp
from routes.categorie import categorie_bp
from routes.auth import utenti_bp
from services.autori_service import get_all_autori
from services.categorie_service import get_all_categorie
from services.utenti_service import get_all_utenti
from flask_login import LoginManager, login_required, current_user


login_manager = LoginManager()
login_manager.login_view = "utenti.login" # type: ignore


app = Flask(__name__)

# Configura il percorso del database SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'libri.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "your_secret_key"


# Inizializza SQLAlchemy
db.init_app(app)
login_manager.init_app(app) # type: ignore

app.register_blueprint(libri_bp,url_prefix= '/api')
app.register_blueprint(categorie_bp,url_prefix= '/api')
app.register_blueprint(utenti_bp,url_prefix= '/api')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)  # Errore 403: Accesso negato
        return f(*args, **kwargs)
    return decorated_function

def bibliotecario_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_bibliotecario:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function
  
@app.route('/home')
@login_required
def form():
    return render_template('form.html')

@app.route('/libri')
@login_required
def libri():
    autori = get_all_autori()
    categorie = get_all_categorie()
    return render_template('libri.html', autori=autori,categorie = categorie)

@app.route('/utenti')
@login_required
def utenti():
    utenti = get_all_utenti()
    return render_template('utenti.html', utenti=utenti)

@app.route('/cerca')
@login_required
@bibliotecario_required
def cerca():
    return render_template('cerca.html')

@app.route('/categorie')
@login_required
def categorie():
    categorie = get_all_categorie()
    return render_template('categorie.html', categorie=categorie)

# Rotta di base per testare il server
@app.route('/')
def home():
    return "Benvenuto nella Libreria API!"

@app.route('/dashboard')
@login_required
def dashboard():
    return "Benvenuto nella tua area personale!"

@login_manager.user_loader
def load_user(user_id):
    return Utente.query.get(int(user_id))


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
app.run(debug=True)