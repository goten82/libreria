from flask import Blueprint, request,render_template

from services.categorie_service import add_categoria, get_all_categorie,delete_categoria

categorie_bp = Blueprint('categorie',__name__)

@categorie_bp.route('/categorie', methods=['GET'])
# ritorna tutti i libri nel db
def get_libri():
    categorie = get_all_categorie()

    return render_template('categorie.html',categorie=categorie)


@categorie_bp.route('/add_categoria', methods=['POST'])
# ritorna tutti i libri nel db
def aggiungi_categoria():
    return add_categoria()


@categorie_bp.route('/del_categoria/<int:id>', methods=['GET'])
def elimina_categoria(id):
    return delete_categoria(id)