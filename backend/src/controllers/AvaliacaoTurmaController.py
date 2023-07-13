import json
from flask import jsonify, request
from ..services.AvaliacaoTurmaService import AvaliacaoTurmaService

class AvaliacaoTurmaController:
    def __init__(self, app, database):
        self.app = app
        self.avaliacao_turma_service = AvaliacaoTurmaService(database)
        self.routes()

    def routes(self):
        @self.app.route('/avaliacao_turma', methods=['GET'])
        def getAllAvaliacaoTurma():
            try:
              result = self.avaliacao_turma_service.read()
              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/avaliacao_turma/<id>', methods=['GET'])
        def getOneAvaliacaoTurmaById(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            try:
              result = self.avaliacao_turma_service.readOne(id)

              if result == None:
                return jsonify({'message': 'Sem Resultados'}), 404 


              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
        
        @self.app.route('/avaliacao_turma', methods=['POST'])
        def postOneAvaliacaoTurma():
            if not request.json:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.avaliacao_turma_service.create(request.json)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/avaliacao_turma/<id>', methods=['PUT'])
        def updateOneAvaliacaoTurma(id):
            if not request.json or not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.avaliacao_turma_service.update(request.json, id)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/avaliacao_turma/<id>', methods=['DELETE'])
        def deleteOneAvaliacaoTurma(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.avaliacao_turma_service.delete(id)

              return jsonify({'message': 'Sucesso'}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
               