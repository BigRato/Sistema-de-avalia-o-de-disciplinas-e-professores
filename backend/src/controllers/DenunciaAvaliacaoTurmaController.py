import json
from flask import jsonify, request
from ..services.DenunciaAvaliacaoTurmaService import DenunciaAvaliacaoTurmaService

class DenunciaAvaliacaoTurmaController:
    def __init__(self, app, database):
        self.app = app
        self.denuncia_avaliacao_turma_service = DenunciaAvaliacaoTurmaService(database)
        self.routes()

    def routes(self):
        @self.app.route('/denuncia_avaliacao_turma', methods=['GET'])
        def getAllDenunciaAvaliacaoTurma():
            try:
              result = self.denuncia_avaliacao_turma_service.read()
              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/denuncia_avaliacao_turma/<id>', methods=['GET'])
        def getOneDenunciaAvaliacaoTurmaById(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            try:
              result = self.denuncia_avaliacao_turma_service.readOne(id)

              if result == None:
                return jsonify({'message': 'Sem Resultados'}), 404 


              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
        
        @self.app.route('/denuncia_avaliacao_turma', methods=['POST'])
        def postOneDenunciaAvaliacaoTurma():
            if not request.json:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.denuncia_avaliacao_turma_service.create(request.json)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
            
        @self.app.route('/denuncia_avaliacao_turma/<id>', methods=['DELETE'])
        def deleteOneDenunciaAvaliacaoTurma(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.denuncia_avaliacao_turma_service.delete(id)

              return jsonify({'message': 'Sucesso'}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
               