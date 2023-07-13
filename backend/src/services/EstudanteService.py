import sys
import json

class EstudanteService:
    def __init__(self, database):
        self.database = database

    def read(self):
      query_string = 'SELECT * FROM ESTUDANTE;'

      results = self.database.query(query_string)

      # o retorno da query é uma lista de tuplas
      # abaixo essa lista de tuplas é convertida em uma lista de dicts

      results_list = []

      for result in results:
        json_response = {
          'id': result[0],
          'nome': result[1],
          'email': result[2],
          'matricula': result[3],
          'senha': result[4],
        }
      
        results_list.append(json_response)

      return results_list
    
    def readOne(self, id):
      # usando %s para evitar que o input do usuário vá direto pra query strint (evitar sql injection)
      query_string = 'SELECT * FROM ESTUDANTE WHERE ID = %s;'

      result = self.database.query_with_params(query_string, (id,))
      if not result:
         return None
      tuple_result = result[0]
      json_response = {
        'id': tuple_result[0],
        'nome': tuple_result[1],
        'email': tuple_result[2],
        'matricula': tuple_result[3],
        'senha': tuple_result[4],
      }

      return json_response
    
    def create(self, data):
      params = (
        data["nome"],
        data["email"],
        data["matricula"],
        data["senha"],
      )

      query_string = \
      """
      INSERT INTO ESTUDANTE (NOME, EMAIL, MATRICULA, SENHA) 
        VALUES (%s, %s, %s, %s);

      """

      result = self.database.query_with_params(query_string, params)
      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
    
    def update(self, data, id):
       
      params = (
        data["nome"],
        data["email"],
        data["matricula"],
        data["senha"],
        int(id)
      )

      query_string = \
      """
      UPDATE ESTUDANTE SET NOME = %s, EMAIL = %s, MATRICULA = %s, SENHA = %s WHERE ID = %s;

      """

      result = self.database.query_with_params(query_string, params)
      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
    
    def delete(self, id):
      query_string = \
      """
      DELETE FROM ESTUDANTE WHERE ID = %s;

      """

      result = self.database.query_with_params(query_string, (int(id),))

      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
      

    





