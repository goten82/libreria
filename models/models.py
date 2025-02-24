from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Autori(db.Model):
    __tablename__ = "autori"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(25))
    cognome = db.Column(db.String(25))
    libri = db.relationship('Libri', backref='autore', lazy=True)

    def __repr__(self):
        return f'<Autore {self.nome} {self.cognome}>'

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome           
        }
    
class Categorie(db.Model):
    __tablename__ = "categorie"

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(25))
    libri = db.relationship('Libri', backref='categoria', lazy=True)

    def __repr__(self):
        return f'<Categoria {self.categoria}>'
    
    def to_dict(self):
        return {
            "id":self.id,
            "categoria": self.categoria
       }

class Libri(db.Model):
    __tablename__ = "libri"

    id = db.Column(db.Integer, primary_key=True)
    titolo = db.Column(db.String(100), nullable=False)
    autore_id = db.Column(db.Integer, db.ForeignKey('autori.id'), nullable=False)
    casa_editrice = db.Column(db.String(50))
    isbn = db.Column(db.String(13))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=False)
    posizione = db.Column(db.String(20))
    prefazione = db.Column(db.String(5000))

    def __repr__(self):
        return f'<Libri {self.titolo}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "titolo": self.titolo,
            "autore_id": self.autore_id,
            "casa_editrice": self.casa_editrice,
            "isbn": self.isbn,
            "categoria_id": self.categoria_id,
            "posizione": self.posizione,
            "prefazione" : self.prefazione
        }

class Utente(db.Model):
    __tablename__ = "utenti"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    ruolo = db.Column(db.String(50), nullable=False, default="utente")  # "admin" | "bibliotecario" | "utente"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
     # Flask-Login methods (grazie a UserMixin vengono automaticamente implementati)
    def get_id(self):
        return str(self.id)

    # Se vuoi ridefinirli manualmente
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_admin(self):
        return self.ruolo == "admin"

    @property
    def is_bibliotecario(self):
        return self.ruolo == "bibliotecario"

