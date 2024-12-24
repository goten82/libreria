from flask import Blueprint, jsonify, request,render_template,redirect,url_for,flash
from models.libri import db,Libri
from services.libri_service import get_all_libri,add_libro,get_libro_by_autore,get_libro_by_titolo,update_libro,get_by_id,delete_libro

libri_bp = Blueprint('libri',__name__)

@libri_bp.route('/libri', methods=['GET'])
# ritorna tutti i libri nel db
def get_libri():
    libri = get_all_libri()
   
    return render_template('elenco_libri.html',libri=libri)

@libri_bp.route('/add_libro', methods=['POST'])
def aggiungi_libro():
    return add_libro()
    
@libri_bp.route('/libro/<int:libro_id>/edit', methods=['GET'])
#cerca libro per id e ritorna la pagina di modifica
def edit_libro(libro_id):
    libro = get_by_id(libro_id)  # Recupera il libro dal database
    return render_template('edit_libro.html', libro=libro)
  

@libri_bp.route('/libro/<int:libro_id>', methods=['GET'])
#cerca libro per id e ritorna la pagina di dettaglio
def get_libro_by_id(libro_id):
   
    libro = get_by_id(libro_id)

    return render_template('dettaglio_libro.html',libro=libro)


@libri_bp.route('/libro',methods=['GET'])
def cerca():
    to_research = request.args['ricerca']
    tipoRicerca = request.args['flexRadioDefault']
    
    if(tipoRicerca=='titolo'):
        libri = get_libro_by_titolo(to_research)
    else:
        libri = get_libro_by_autore(to_research)
    
    return render_template('elenco_libri.html',libri=libri)

@libri_bp.route('/update_libro/<int:libro_id>', methods=['POST'])
def aggiorna_libro(libro_id):
    return update_libro(libro_id)


@libri_bp.route('/delete_libro/<int:libro_id>', methods=['DELETE'])
def elimina_libro(libro_id):
    return delete_libro(libro_id)