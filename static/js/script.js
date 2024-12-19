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

let btnInserisci = document.getElementById('inserisci');
let btnCercaLibro = document.getElementById('cercaLibro');
let btnApriInserisci = document.getElementById('apri_inserisci');
let btnElenco = document.getElementById('lista');
let btnChiudi = document.getElementById('chiudi');


if (btnApriInserisci != null) {
    btnApriInserisci.addEventListener('click', ev => {
        document.getElementById('form_inserisci').style.display = '';
    });
}

if (btnInserisci != null) {
    btnInserisci.addEventListener('click', ev => {
        inserisciLibro(ev);
    });
}

if (btnCercaLibro != null) {
    btnCercaLibro.addEventListener('click', ev => {
        cercaLibro();
    });
}

if (btnElenco != null) {
    btnElenco.addEventListener('click', ev => {
        visualizzaListaLibri();
    });
}
if (btnChiudi != null) {
    btnChiudi.addEventListener('click', ev => {
        window.location.href = '/home';
    });
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

function modificaLibro(id){
    
}

async function inserisciLibro(event) {
    event.preventDefault();
    let titolo = document.getElementById('titolo').value;
    let autore = document.getElementById('autore').value;
    let casa_editrice = document.getElementById('editrice').value;
    let isbn = document.getElementById('isbn').value;
    let categoria = document.getElementById('categoria').value;
    const libro = new Libri(titolo, autore, casa_editrice, isbn, categoria);
    verificaDati(libro);
    await fetch('/api/add_libro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            titolo: titolo,
            autore: autore,
            casa_editrice: casa_editrice,
            isbn: isbn,
            categoria: categoria
        })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('messageInsert').innerHTML = data.message
        })
        .catch((error) => {
            document.getElementById('messageInsert').innerHTML = error;
        }).finally(() => {
            svuotaCampi();
        });
}

async function visualizzaListaLibri() {
    let response = await fetch('/api/libri', {
        method: 'GET'
    });
    if (response.status == 200) {
        const libri = await response.json();
        libri.forEach(element => {
            document.getElementById('tabellaLibri').innerHTML += `
                        <tr>
                            <td>${element.titolo}</td>
                            <td>${element.autore}</td>
                            <td>${element.casa_editrice}</td>
                            <td>${element.isbn}</td>
                            <td>${element.categoria}</td>
                            <td>
                                <a href="/libri/${element.id}" class="btn btn-primary btn-sm">Dettagli</a>
                                <a href="/libri/${element.id}/edit" class="btn btn-warning btn-sm"><i class="fa-solid fa-trash">Modifica</i></a>
                                <a href="/libri/${element.id}/delete" class="btn btn-danger btn-sm">Elimina</a>
                            </td>
                        </tr>`
        });
        document.getElementById('divTabella').style.display = '';
    }
}

function svuotaCampi() {
    document.getElementById('titolo').value = '';
    document.getElementById('autore').value = '';
    document.getElementById('editrice').value = '';
    document.getElementById('isbn').value = '';
    document.getElementById('categoria').value = '';
}

function verificaDati(libro) {
    if (libro.titolo == '' && libro.autore == '') {
        alert("Nessun titolo specificato");
        throw TypeError("Nessun titolo specificato");

    }
}
async function cercaLibro() {

    let titolo = document.getElementById('titolo_find').value;

    if (titolo == '') {
        console.error('Inserire un titolo');
        throw TypeError("Inserire un titolo'");
    }
    let response = await fetch('/api/libro/titolo/' + titolo, {
        method: 'GET'
    });

    const result = await response.json(); // Parsa il JSON
    if (response.status == 200) {
        document.getElementById('resTitolo').innerHTML = `
                    <p>Titolo: <strong>${result.titolo}</strong></p>
                    <p>Autore: <strong>${result.autore}</strong></p>
                    <p>Casa editrice: <strong>${result.casa_editrice}</strong></p>
                    <p>ISBN: <strong>${result.isbn}</strong></p>
                    <p>Categoria: <strong>${result.categoria}</strong></p>
                    `;
    }
    else {
        document.getElementById('resTitolo').innerHTML = `${result.message}`;
    }
    document.getElementById('resTitolo').style.display = 'block';
}

document.getElementById('chiudiCercaTitolo').addEventListener('click', ev => {
    document.getElementById('titolo_find').value = '';
    document.getElementById('resTitolo').style.display = 'none';

});

document.getElementById('CercaAutore').addEventListener('click', ev => {
    cercaLibriAutore();
});

async function cercaLibriAutore() {
    let autore = document.getElementById('find_autore').value;

    if (autore == '') {
        console.error('Inserire un autore');
        throw TypeError("Inserire un autore");
    }

    let response = await fetch('/api/libro/autore/' + autore, {
        method: 'GET'
    });

    const result = await response.json();
    if (response.status == 200) {

        document.getElementById('resAutore').style.display = 'block';
        document.getElementById('resAutore').innerHTML = `<h2>Elenco</h2>
            <table id="tabella">
                <thead>
                    <tr>
                        <th>Titolo</th>
                        <th>Autore</th>
                        <th>Casa editrice</th>
                        <th>ISBN</th>
                        <th>Categoria</th>
                    </tr>
                </thead>
                <tbody class="righe">

                </tbody>
            </table>
            `;
        let tabella = document.getElementById('tabella');
        let righe = tabella.getElementsByClassName('righe').item('tbody');
        let testo = '';
        result.forEach(element => {

            testo += `
                    <tr id="libri" data-id='${element.id}'>
                      <td>${element.titolo}</td>
                      <td>${element.autore} </td>
                      <td>${element.casa_editrice}</td>   
                      <td>${element.isbn}</td> 
                      <td>${element.categoria}</td> 
                    </tr>
                `;

            righe.innerHTML = testo;
        });
    } else {
        document.getElementById('resAutore').innerHTML = `${result.message}`;
    }
    document.getElementById('resAutore').style.display = 'block';
}

document.getElementById('chiudiCercaAutore').addEventListener('click', ev => {
    document.getElementById('find_autore').value = '';
    document.getElementById('resAutore').style.display = 'none';
});
