from flask import render_template, redirect, url_for, flash, request,Blueprint
from flask_login import login_user, logout_user, login_required
from models.models import db, Utente
from werkzeug.security import check_password_hash, generate_password_hash

utenti_bp = Blueprint('utenti',__name__)

@utenti_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Utente.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Login effettuato con successo!', 'success')
            return redirect(url_for('form'))
        else:
            flash('Email o password errati.', 'danger')

    return render_template('login.html')

@utenti_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Controllo sicurezza password
        error = is_password_secure(password)
        if error:
            flash(error, "danger")
            return redirect(url_for("utenti.register"))

        # Hash della password e salvataggio nel database
        hashed_password = generate_password_hash(password)
        nuovo_utente = Utente(username=username, email=email, password_hash=hashed_password) # type: ignore
        db.session.add(nuovo_utente)
        db.session.commit()

        flash("Registrazione completata!", "success")
        return redirect(url_for("utenti.login"))

    return render_template('register.html')

@utenti_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout effettuato.', 'info')
    return redirect(url_for('utenti.login'))


import re

def is_password_secure(password):
    """Verifica se la password rispetta i criteri di sicurezza."""
    if len(password) < 8:
        return "La password deve avere almeno 8 caratteri."
    if not re.search(r'[A-Z]', password):
        return "La password deve contenere almeno una lettera maiuscola."
    if not re.search(r'[a-z]', password):
        return "La password deve contenere almeno una lettera minuscola."
    if not re.search(r'[0-9]', password):
        return "La password deve contenere almeno un numero."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "La password deve contenere almeno un carattere speciale (!@#$%^&*)."
    
    return None  # Nessun errore, password valida