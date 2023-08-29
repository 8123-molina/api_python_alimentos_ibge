from flask import  abort,jsonify
from flask_restapi import Resource

from alimentos.models import AlimentosModel

# busca todos alimentos
Class Alimentos(Resource):
    def get(self):
        alimentos = Alimentos.query.all() or abort(204) 
        return jsonify(
            {"alimentos":[alimentos.to_dict() for alimentos in alimentos]}
            
        )


