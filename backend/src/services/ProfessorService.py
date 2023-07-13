import sys
import json

class ProfessorService:
    def __init__(self, database):
        self.database = database

    def read(self):
      query_string = 'SELECT * FROM PROFESSOR;'

      results = self.database.query(query_string)

      # o retorno da query é uma lista de tuplas
      # abaixo essa lista de tuplas é convertida em uma lista de dicts

      results_list = []

      for result in results:
        json_response = {
          'id': result[0],
          'nome': result[1],
          'departamento_id': result[2],
          'foto': result[3],
        }
      
        results_list.append(json_response)

      return results_list
    
    def readOne(self, id):
      # usando %s para evitar que o input do usuário vá direto pra query strint (evitar sql injection)
      query_string = 'SELECT * FROM PROFESSOR WHERE ID = %s;'

      result = self.database.query_with_params(query_string, (id,))
      if not result:
         return None
      tuple_result = result[0]
      json_response = {
        'id': tuple_result[0],
        'nome': tuple_result[1],
        'departamento_id': tuple_result[2],
        'foto': tuple_result[3],
        
      }

      return json_response
    
    def create(self, data):
      params = (
        data["nome"],
        data["departamento_id"],
        data["foto"],
      )

      query_string = \
      """
      INSERT INTO PROFESSOR (NOME, DEPARTAMENTO_ID, FOTO) 
        VALUES (%s, %s, %s);

      """

      result = self.database.query_with_params(query_string, params)
      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
    
    def update(self, data, id):
       
      params = (
        data["nome"],
        data["departamento_id"],
        data["foto"],
        int(id)
      )

      query_string = \
      """
      UPDATE PROFESSOR SET NOME = %s, DEPARTAMENTO_ID = %s, FOTO = %s WHERE ID = %s;

      """

      result = self.database.query_with_params(query_string, params)
      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
    
    def delete(self, id):
      query_string = \
      """
      DELETE FROM PROFESSOR WHERE ID = %s;

      """

      result = self.database.query_with_params(query_string, (int(id),))

      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
      

    





