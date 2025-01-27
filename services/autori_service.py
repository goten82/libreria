from flask import jsonify, request,redirect,url_for,flash
from models.models import Autori

def get_all_autori():
    return Autori.query.all()

def get_by_nominativo(nome, cognome):
    pass