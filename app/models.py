from . import db
from flask import current_app, request


class Personaggio(db.Model):
    __tablename__ = 'personaggi'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True)
    quantita = db.Column(db.Integer)
    tipologia_id = db.Column(db.Integer, db.ForeignKey('tipologie.id'))
    allineamento_id = db.Column(db.Integer, db.ForeignKey('allineamenti.id'))
    descrizione = db.Column(db.Text())


class Tipologia(db.Model):
    __tablename__ = 'tipologie'
    id = db.Column(db.Integer, primary_key=True)
    tipologia = db.Column(db.String(100))
    personaggi = db.relationship('Personaggio', backref='tipologia', lazy='dynamic')


class Allineamento(db.Model):
    __tablename__ = 'allineamenti'
    id = db.Column(db.Integer, primary_key=True)
    allineamento = db.Column(db.String(100))
    personaggi = db.relationship('Personaggio', backref='allineamento', lazy='dynamic')
