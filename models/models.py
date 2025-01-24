from flask_sqlalchemy import SQLAlchemy

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

class Libri(db.Model):
    __tablename__ = "libri"

    id = db.Column(db.Integer, primary_key=True)
    titolo = db.Column(db.String(100), nullable=False)
    autore_id = db.Column(db.Integer, db.ForeignKey('autori.id'), nullable=False)
    casa_editrice = db.Column(db.String(50))
    isbn = db.Column(db.String(13))
    categoria = db.Column(db.String(50))
    posizione = db.Column(db.String(20))

    def __repr__(self):
        return f'<Libri {self.titolo}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "titolo": self.titolo,
            "autore_id": self.autore_id,
            "casa_editrice": self.casa_editrice,
            "isbn": self.isbn,
            "categoria": self.categoria,
            "posizione": self.posizione
        }
