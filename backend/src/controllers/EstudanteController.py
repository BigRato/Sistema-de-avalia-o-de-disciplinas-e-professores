import json
from flask import jsonify, request
from ..services.EstudanteService import EstudanteService

class EstudanteController:
    def __init__(self, app, database):
        self.app = app
        self.estudante_service = EstudanteService(database)
        self.routes()

    def routes(self):
        @self.app.route('/estudante', methods=['GET'])
        def getAllEstudantes():
            try:
              result = self.estudante_service.read()
              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/estudante/<id>', methods=['GET'])
        def getOneEstudanteById(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            try:
              result = self.estudante_service.readOne(id)

              if result == None:
                return jsonify({'message': 'Sem Resultados'}), 404 


              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
        
        @self.app.route('/estudante', methods=['POST'])
        def postOneEstudante():
            if not request.json:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.estudante_service.create(request.json)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/estudante/<id>', methods=['PUT'])
        def updateOneEstudante(id):
            if not request.json or not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.estudante_service.update(request.json, id)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/estudante/<id>', methods=['DELETE'])
        def deleteOneEstudante(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.estudante_service.delete(id)

              return jsonify({'message': 'Sucesso'}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
               