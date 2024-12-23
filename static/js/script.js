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
