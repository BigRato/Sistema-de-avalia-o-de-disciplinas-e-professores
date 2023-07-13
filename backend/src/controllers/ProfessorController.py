import json
from flask import jsonify, request
from ..services.ProfessorService import ProfessorService

class ProfessorController:
    def __init__(self, app, database):
        self.app = app
        self.professor_service = ProfessorService(database)
        self.routes()

    def routes(self):
        @self.app.route('/professor', methods=['GET'])
        def getAllProfessor():
            try:
              result = self.professor_service.read()
              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/professor/<id>', methods=['GET'])
        def getOneProfessorById(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            try:
              result = self.professor_service.readOne(id)

              if result == None:
                return jsonify({'message': 'Sem Resultados'}), 404 


              return jsonify({'message': 'Sucesso',
                              'data': result}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
        
        @self.app.route('/professor', methods=['POST'])
        def postOneProfessor():
            if not request.json:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.professor_service.create(request.json)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/professor/<id>', methods=['PUT'])
        def updateOneProfessor(id):
            if not request.json or not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.professor_service.update(request.json, id)

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
        @self.app.route('/professor/<id>', methods=['DELETE'])
        def deleteOneProfessor(id):
            if not id:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              self.professor_service.delete(id)

              return jsonify({'message': 'Sucesso'}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
               
