from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Libri(db.Model):
    __tablename__ = "libri"

    id = db.Column(db.Integer, primary_key=True)
    titolo = db.Column(db.String(100), nullable=False)
    autore = db.Column(db.String(50), )
    casa_editrice = db.Column(db.String(50))
    isbn = db.Column(db.String(13))
    categoria = db.Column(db.String(50))
    posizione = db.Column(db.String(20))

    def __repr__(self):
        return f'<Libri {self.titolo} di  {self.autore}>'
    
    def to_dict(self):
        return{
            "id":self.id,
            "titolo": self.titolo,
            "autore": self.autore,
            "casa_editrice": self.casa_editrice,
            "isbn":self.isbn,
            "categoria": self.categoria,
            "posizione":self.posizione
        }