from models.libri import db,Libri

#inserimento libro
def add_libro(titolo, autore, casa_editrice, isbn, categoria):
    libro = Libri(
        titolo=titolo,  # type: ignore
        autore=autore, # type: ignore
        casa_editrice=casa_editrice,# type: ignore
        isbn=isbn,# type: ignore
        categoria=categoria# type: ignore
        ) 
    db.session.add(libro) 
    db.session.commit()     

    return libro
