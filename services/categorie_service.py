from flask import jsonify, request,redirect,url_for,flash
from models.models import Categorie,db

def get_all_categorie():
    return Categorie.query.all()

def add_categoria():
    categoria = request.form['categoria']

    new_categoria = Categorie(categoria=categoria) # type: ignore
    db.session.add(new_categoria)
    db.session.commit()

    flash("Categoria inserita con successo!", "success")
    return redirect(url_for('categorie'))

def delete_categoria(id):
    categoria = Categorie.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    
    flash("Categoria eliminata con successo!", "success")
    return redirect(url_for('categorie'))
