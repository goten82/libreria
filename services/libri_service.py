from flask import jsonify, request,redirect,url_for,flash
from models.models import Autori, Libri,Categorie,db

def get_all_libri():
    return Libri.query.all()

def get_by_id(id):
    return Libri.query.get_or_404(id)


#inserimento libro
def add_libro():
    data = request.form
    titolo = data['titolo']
    autore_id = data['autore_id']
    casa_editrice = data['casa_editrice']
    isbn = data['isbn']
    categoria = data['categoria']
    categoria_id = data['categoria_id']
    posizione = data['posizione'] 
    nome = data['nome']
    cognome  = data['cognome']

    if nome and cognome:
        autore = Autori.query.filter_by(nome=nome,cognome=cognome).first()
        if not autore:
            autore = Autori(nome=nome,cognome=cognome)# type: ignore
            db.session.add(autore)
            db.session.commit()
        autore_id = autore.id

    if categoria:
        _categoria = Categorie.query.filter_by(categoria=categoria).first()
        if not _categoria:
            new_categoria = Categorie(categoria=categoria)# type: ignore
            db.session.add(new_categoria)
            db.session.commit()
        categoria_id = new_categoria.id

    new_libro = Libri(
        titolo=titolo, # type: ignore
        autore_id=autore_id, # type: ignore
        casa_editrice=casa_editrice, # type: ignore
        isbn=isbn, # type: ignore
        categoria_id=categoria_id, # type: ignore
        posizione=posizione # type: ignore  
    )    
    db.session.add(new_libro)
    db.session.commit()

    
    flash("Libro inserito con successo!", "success")
    return redirect(url_for('libri.get_libri'))

def get_libro_by_titolo(titolo):
    return Libri.query.filter(Libri.titolo.ilike(f"%{titolo}%")).all()

# def get_libro_by_autore(autore):
#     return Libri.query.filter(Libri.autore.ilike(f"%{autore}%")).all()

def update_libro(id):
    libro = get_by_id(id) # Cerca l'utente per ID

     # Aggiorna i campi dell'utente
    
    libro.titolo=request.form['titolo']  # type: ignore
    libro.autore_id=request.form['autore_hidden']# type: ignore
    libro.casa_editrice=request.form['casa_editrice'] # type: ignore
    libro.isbn=request.form['isbn'] # type: ignore
    libro.categoria_id=request.form['categoria_id'] # type: ignore
    libro.posizione=request.form['posizione']
    
    db.session.commit()  # Salva le modifiche nel database
    flash("Libro aggiornato con successo!", "success")
    return redirect(url_for('libri.get_libri'))

def delete_libro(id):
    libro = get_by_id(id)

    db.session.delete(libro)  # Elimina l'utente dal database
    db.session.commit()

    return jsonify({"message": "Libro eliminato con successo!"})