from flask import Blueprint, request,render_template
from flask_login import  login_required

from services.libri_service import get_all_libri,add_libro,get_libro_by_titolo,update_libro,get_by_id,delete_libro
from services.categorie_service import get_all_categorie

libri_bp = Blueprint('libri',__name__)

@libri_bp.route('/libri', methods=['GET'])
@login_required
# ritorna tutti i libri nel db
def get_libri():

    libri = get_all_libri()   
    return render_template('elenco_libri.html',libri=libri)

@libri_bp.route('/add_libro', methods=['POST'])
@login_required
def aggiungi_libro():
    return add_libro()
    
@libri_bp.route('/libro/<int:libro_id>/edit', methods=['GET'])
#cerca libro per id e ritorna la pagina di modifica
def edit_libro(libro_id):

    libro = get_by_id(libro_id)  # Recupera il libro dal database
    categorie = get_all_categorie()    
    return render_template('edit_libro.html', libro=libro, categorie=categorie)
  

@libri_bp.route('/libro/<int:libro_id>', methods=['GET'])
@login_required
#cerca libro per id e ritorna la pagina di dettaglio
def get_libro_by_id(libro_id):
   
    libro = get_by_id(libro_id)
    return render_template('dettaglio_libro.html',libro=libro)


@libri_bp.route('/libro',methods=['GET'])
@login_required
def cerca():
    to_research = request.args['ricerca']
    tipoRicerca = request.args['flexRadioDefault']
    
    if(tipoRicerca=='titolo'):
        libri = get_libro_by_titolo(to_research)
    # else:
    #     libri = get_libro_by_autore(to_research)
    
    return render_template('elenco_libri.html',libri=libri)

@libri_bp.route('/update_libro/<int:libro_id>', methods=['POST'])
@login_required
def aggiorna_libro(libro_id):
    return update_libro(libro_id)


@libri_bp.route('/delete_libro/<int:libro_id>', methods=['DELETE'])
@login_required
def elimina_libro(libro_id):
    return delete_libro(libro_id)