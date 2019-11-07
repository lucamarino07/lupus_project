from flask import jsonify
from . import main
from .. import db
from ..models import Personaggio


@main.route('/personaggi', methods=["GET"])
def index():
    personaggi = Personaggio.query.all()
    response = []
    for personaggio in personaggi:
        for i in range(1, personaggio.quantita + 1):

            personaggio_response = {
                'nome': personaggio.nome,
                'progressivo': i,
                'tipologia': personaggio.tipologia.tipologia,
                'allineamento': personaggio.allineamento.allineamento,
                'descrizione': personaggio.descrizione,
            }
            response.append(personaggio_response)

    return jsonify({'personaggi': response})
