import sys
import json

class AvaliacaoProfessorService:
    def __init__(self, database):
        self.database = database

    def read(self):
      query_string = 'SELECT * FROM AVALIACAO_PROFESSOR;'

      results = self.database.query(query_string)

      # o retorno da query é uma lista de tuplas
      # abaixo essa lista de tuplas é convertida em uma lista de dicts

      results_list = []

      for result in results:
        json_response = {
          'id': result[0],
          'texto': result[1],
          'likes': result[2],
          'dislikes': result[3],
          'denuncias': result[4],
          'estudante_id': result[5],
          'professor_id': result[6],
        }
      
        results_list.append(json_response)

      return results_list
    
    def readOne(self, id):
      # usando %s para evitar que o input do usuário vá direto pra query strint (evitar sql injection)
      query_string = 'SELECT * FROM AVALIACAO_PROFESSOR WHERE ID = %s;'

      result = self.database.query_with_params(query_string, (id,))
      if not result:
         return None
      tuple_result = result[0]
      json_response = {
        'id': tuple_result[0],
        'texto': tuple_result[1],
        'likes': tuple_result[2],
        'dislikes': tuple_result[3],
        'denuncias': tuple_result[4],
        'estudante_id': tuple_result[5],
        'professor_id': tuple_result[6],
      }

      return json_response
    
    def create(self, data):
      params = (
        data["texto"],
        data["estudante_id"],
        data["professor_id"],
      )

      query_string = \
      """
      INSERT INTO AVALIACAO_PROFESSOR (TEXTO, ESTUDANTE_ID, PROFESSOR_ID) 
        VALUES (%s, %s, %s);

      """

      result = self.database.query_with_params(query_string, params)
      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
    
    def update(self, data, id):
       
      params = (
        data["texto"],
  
        int(id)
      )

      query_string = \
      """
      UPDATE AVALIACAO_PROFESSOR SET TEXTO = %s WHERE ID = %s;

      """

      result = self.database.query_with_params(query_string, params)
      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
    
    def delete(self, id):
      query_string = \
      """
      DELETE FROM AVALIACAO_PROFESSOR WHERE ID = %s;

      """

      result = self.database.query_with_params(query_string, (int(id),))

      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
      

    





