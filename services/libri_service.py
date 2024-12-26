from flask import Blueprint, jsonify, request,render_template,redirect,url_for,flash
from models.libri import db,Libri

def get_all_libri():
    return Libri.query.all()

def get_by_id(id):
    return Libri.query.get_or_404(id)


#inserimento libro
def add_libro():
    data = request.form
    new_libro = Libri(
        titolo=data['titolo'],  # type: ignore
        autore=data['autore'], # type: ignore
        casa_editrice=data['casa_editrice'], # type: ignore
        isbn=data['isbn'], # type: ignore
        categoria=data['categoria'], # type: ignore
        posizione=data['posizione'] #type: ignore
    )    
    db.session.add(new_libro)
    db.session.commit()
    flash("Libro inserito con successo!", "success")
    return redirect(url_for('libri.get_libri'))

def get_libro_by_titolo(titolo):
    return Libri.query.filter(Libri.titolo.ilike(f"%{titolo}%")).all()

def get_libro_by_autore(autore):
    return Libri.query.filter(Libri.autore.ilike(f"%{autore}%")).all()

def update_libro(id):
    libro = get_by_id(id) # Cerca l'utente per ID

     # Aggiorna i campi dell'utente
    
    libro.titolo=request.form['titolo']  # type: ignore
    libro.autore=request.form['autore']# type: ignore
    libro.casa_editrice=request.form['casa_editrice'] # type: ignore
    libro.isbn=request.form['isbn'] # type: ignore
    libro.categoria=request.form['categoria'] # type: ignore
    libro.posizione=request.form['posizione']
    
    db.session.commit()  # Salva le modifiche nel database
    flash("Libro aggiornato con successo!", "success")
    return redirect(url_for('libri.get_libri'))

def delete_libro(id):
    libro = get_by_id(id)

    db.session.delete(libro)  # Elimina l'utente dal database
    db.session.commit()

    return jsonify({"message": "Libro eliminato con successo!"})