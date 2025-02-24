from flask import jsonify, request,redirect,url_for,flash
from models.models import Utente,db

def get_all_utenti():
    return Utente.query.all()