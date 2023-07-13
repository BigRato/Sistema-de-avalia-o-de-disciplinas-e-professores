import json
from flask import jsonify, request
from ..services.LoginService import LoginService

class LoginController:
    def __init__(self, app, database):
        self.app = app
        self.login_service = LoginService(database)
        self.routes()

    def routes(self):
        
        @self.app.route('/login', methods=['POST'])
        def login():
            if not request.json:
              return jsonify({'message': 'Os dados não foram passados'}), 400
            
            try:
              result = self.login_service.login(request.json)

              if not result:
                 return jsonify({'message': 'Email e/ou senha incorreto(s)'}), 401

              return jsonify({'message': 'Sucesso',
                              'data': request.json}), 200
            except Exception as e:
                return jsonify({'message': 'Erro',
                              'error_message': e}), 500
            
       
            
        