import sys
import json

class DenunciaAvaliacaoProfessorService:
    def __init__(self, database):
        self.database = database

    def read(self):
      query_string = 'SELECT * FROM DENUNCIA_AVALIACAO_PROFESSOR;'

      results = self.database.query(query_string)

      # o retorno da query é uma lista de tuplas
      # abaixo essa lista de tuplas é convertida em uma lista de dicts

      results_list = []

      for result in results:
        json_response = {
          'id': result[0],
          'avaliacao_professor_id': result[1],
          'estudante_id': result[2],
        }
      
        results_list.append(json_response)

      return results_list
    
    def readOne(self, id):
      # usando %s para evitar que o input do usuário vá direto pra query strint (evitar sql injection)
      query_string = 'SELECT * FROM DENUNCIA_AVALIACAO_PROFESSOR WHERE ID = %s;'

      result = self.database.query_with_params(query_string, (id,))
      if not result:
         return None
      tuple_result = result[0]
      json_response = {
        'id': tuple_result[0],
        'avaliacao_professor_id': tuple_result[1],
        'estudante_id': tuple_result[2],
      }

      return json_response
    
    def create(self, data):
      params = (
        data["avaliacao_professor_id"],
        data["estudante_id"],
      )

      query_string = \
      """
      INSERT INTO DENUNCIA_AVALIACAO_PROFESSOR (AVALIACAO_PROFESSOR_ID, ESTUDANTE_ID) 
        VALUES (%s, %s);

      """

      result = self.database.query_with_params(query_string, params)
      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
    
   
    
    def delete(self, id):
      query_string = \
      """
      DELETE FROM DENUNCIA_AVALIACAO_PROFESSOR WHERE ID = %s;

      """

      result = self.database.query_with_params(query_string, (int(id),))

      self.database.commit()
      print(result, file=sys.stderr)
       
      return result
      

    





