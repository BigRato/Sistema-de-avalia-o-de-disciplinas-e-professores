import json
from flask import jsonify, request
from ..services.AvaliacaoProfessorService import AvaliacaoProfessorService

class AvaliacaoProfessorController:
    def __init__(self, app, database):
        self.app = app
        self.avaliacao_professor_service = AvaliacaoProfessorService(database)
        self.routes()

    def routes(self):
        @self.app.route('/avaliacao_professor', methods=['GET'])
        def getAllAvaliacaoProfessor():
            try:
              result = self.avaliacao_professor_service.read()
              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/avaliacao_professor/<id>', methods=['GET'])
        def getOneAvaliacaoProfessorById(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            try:
              result = self.avaliacao_professor_service.readOne(id)

              if result == None:
                return jsonify({'message': 'Sem Resultados'}), 404 


              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
        
        @self.app.route('/avaliacao_professor', methods=['POST'])
        def postOneAvaliacaoProfessor():
            if not request.json:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.avaliacao_professor_service.create(request.json)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/avaliacao_professor/<id>', methods=['PUT'])
        def updateOneAvaliacaoProfessor(id):
            if not request.json or not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.avaliacao_professor_service.update(request.json, id)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/avaliacao_professor/<id>', methods=['DELETE'])
        def deleteOneAvaliacaoProfessor(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.avaliacao_professor_service.delete(id)

              return jsonify({'message': 'Sucesso'}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
               