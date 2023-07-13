import json
from flask import jsonify, request
from ..services.DenunciaAvaliacaoProfessorService import DenunciaAvaliacaoProfessorService

class DenunciaAvaliacaoProfessorController:
    def __init__(self, app, database):
        self.app = app
        self.denuncia_avaliacao_professor_service = DenunciaAvaliacaoProfessorService(database)
        self.routes()

    def routes(self):
        @self.app.route('/denuncia_avaliacao_professor', methods=['GET'])
        def getAllDenunciaAvaliacaoProfessor():
            try:
              result = self.denuncia_avaliacao_professor_service.read()
              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/denuncia_avaliacao_professor/<id>', methods=['GET'])
        def getOneDenunciaAvaliacaoProfessorById(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            try:
              result = self.denuncia_avaliacao_professor_service.readOne(id)

              if result == None:
                return jsonify({'message': 'Sem Resultados'}), 404 


              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
        
        @self.app.route('/denuncia_avaliacao_professor', methods=['POST'])
        def postOneDenunciaAvaliacaoProfessor():
            if not request.json:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.denuncia_avaliacao_professor_service.create(request.json)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
            
        @self.app.route('/denuncia_avaliacao_professor/<id>', methods=['DELETE'])
        def deleteOneDenunciaAvaliacaoProfessor(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.denuncia_avaliacao_professor_service.delete(id)

              return jsonify({'message': 'Sucesso'}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
               