from flask import Blueprint, jsonify, request,render_template,redirect,url_for,flash
from models.libri import db,Libri

def get_all_libri():
    return Libri.query.all()


#inserimento libro
def add_libro():
    data = request.form
    new_libro = Libri(
        titolo=data['titolo'],  # type: ignore
        autore=data['autore'], # type: ignore
        casa_editrice=data['casa_editrice'], # type: ignore
        isbn=data['isbn'], # type: ignore
        categoria=data['categoria'] # type: ignore
    )    
    db.session.add(new_libro)
    db.session.commit()
    flash("Libro inserito con successo!", "success")
    return redirect(url_for('libri.get_libri'))

def get_libro_by_titolo(titolo):
    return Libri.query.filter(Libri.titolo.ilike(f"%{titolo}%")).all()

def get_libro_by_autore(autore):
    return Libri.query.filter(Libri.autore.ilike(f"%{autore}%")).all()