from flask import render_template, redirect, url_for, flash, request,Blueprint
from flask_login import login_user, logout_user, login_required
from models.models import db, Utente
from werkzeug.security import check_password_hash

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
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if Utente.query.filter_by(email=email).first():
            flash('Email già in uso.', 'danger')
            return redirect(url_for('utenti.register'))

        new_user = Utente(username=username, email=email) # type: ignore
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registrazione completata! Ora puoi accedere.', 'success')
        return redirect(url_for('utenti.login'))

    return render_template('register.html')

@utenti_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout effettuato.', 'info')
    return redirect(url_for('utenti.login'))
