from flask import Blueprint, jsonify, request,render_template,redirect,url_for,flash
from models.libri import db,Libri

LIBRO_NOT_FOUND = "Libro non trovato!"

libri_bp = Blueprint('libri',__name__)

@libri_bp.route('/add_libro', methods=['POST'])
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

@libri_bp.route('/libri', methods=['GET'])
# ritorna tutti i libri nel db
def get_libri():
    libri = Libri.query.all()
   
    return render_template('elenco_libri.html',libri=libri)

@libri_bp.route('/libro/<int:libro_id>/edit', methods=['GET'])
#cerca libro per id e ritorna la pagina di modifica
def edit_libro(libro_id):
    libro = Libri.query.get_or_404(libro_id)  # Recupera il libro dal database
    return render_template('edit_libro.html', libro=libro)
  

@libri_bp.route('/libro/<int:libro_id>', methods=['GET'])
#cerca libro per id e ritorna la pagina di dettaglio
def get_libro_by_id(libro_id):
   
    libro = Libri.query.get(libro_id)  # Cerca il libro in base all'ID
    if not libro:
        return jsonify({"message": LIBRO_NOT_FOUND}), 404

    return render_template('dettaglio_libro.html',libro=libro)

@libri_bp.route('/libro/autore/<string:libro_autore>', methods=['GET'])
def get_libro_by_autore(libro_autore):

    libri = Libri.query.filter(Libri.autore.ilike(f"%{libro_autore}%")).all()  # Cerca l'utente in base all'ID filter_by(name=name).first()
    if not libri:
        return jsonify({"message": LIBRO_NOT_FOUND}), 404

    return jsonify([libro.to_dict() for libro in libri])

@libri_bp.route('/libro/titolo/<string:libro_titolo>', methods=['GET'])
def get_libro_by_titolo(libro_titolo):
 
    libro = Libri.query.filter_by(titolo=libro_titolo).first()  # Cerca l'utente in base all'ID filter_by(name=name).first()
    if not libro:
        return jsonify({"message": LIBRO_NOT_FOUND}), 404

    return jsonify(libro.to_dict())

@libri_bp.route('/update_libro/<int:libro_id>', methods=['POST'])
def update_libro(libro_id):
    libro = Libri.query.get_or_404(libro_id)  # Cerca l'utente per ID

     # Aggiorna i campi dell'utente
    
    libro.titolo=request.form['titolo']  # type: ignore
    libro.autore=request.form['autore']# type: ignore
    libro.casa_editrice=request.form['casa_editrice'] # type: ignore
    libro.isbn=request.form['isbn'] # type: ignore
    libro.categoria=request.form['categoria'] # type: ignore
    
    db.session.commit()  # Salva le modifiche nel database
    flash("Libro aggiornato con successo!", "success")
    return redirect(url_for('libri.get_libri'))


@libri_bp.route('/delete_libro/<int:libro_id>', methods=['DELETE'])
def delete_libro(libro_id):
    libro = Libri.query.get(libro_id)
    if not libro:
        return jsonify({"message": LIBRO_NOT_FOUND}), 404

    db.session.delete(libro)  # Elimina l'utente dal database
    db.session.commit()

    return jsonify({"message": "Libro eliminato con successo!"})