import sys
import json

class LoginService:
    def __init__(self, database):
        self.database = database

    def login(self, data):
      print(data, file=sys.stderr)
      query_string = 'SELECT * FROM ESTUDANTE WHERE EMAIL = %s AND SENHA = %s;'

      params = (
        data['email'],
        data['senha']
      )
      results = self.database.query_with_params(query_string, params)

      if results == []:
         return None    

      return data['email']
    
    
    





