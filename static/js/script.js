class Libri {
    constructor(titolo, autore, casa_editrice, isbn, categoria) {
        this.titolo = titolo;
        this.autore = autore;
        this.casa_editrice = casa_editrice;
        this.isbn = isbn;
        this.categoria = categoria;
    }

    getTitolo() {
        return this.titolo;
    }

    getAutore() {
        return this.autore;
    }

    getCasaEditrice() {
        return this.casa_editrice;
    }

    getIsbn() {
        return this.isbn;
    }

    getCategoria() {
        return this.categoria;
    }

    setTitolo(titolo) {
        this.titolo = titolo;
    }

    setAutore(autore) {
        this.autore = autore;
    }

    setCasaEditrice(casa_editrice) {
        this.casa_editrice = casa_editrice;
    }

    setIsbn(isbn) {
        this.isbn = isbn;
    }

    setCategoria(categoria) {
        this.categoria = categoria;
    }
}

function eliminaLibro(id) {
    if (confirm("Sei sicuro di voler eliminare questo libro?")) {
        fetch(`/api/delete_libro/${id}`, {
            method: 'DELETE'
        }).then(response => {
            if (response.ok) {
                alert("Libro eliminato con successo!");
                location.reload(); // Ricarica la pagina
            } else {
                alert("Errore durante l'eliminazione del libro.");
            }
        });
    }
}