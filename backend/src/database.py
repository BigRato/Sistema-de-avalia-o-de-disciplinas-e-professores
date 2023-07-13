import os
import sys
import psycopg2

class Database():
  def __init__(self):
    self.connection = psycopg2.connect(
      host=os.environ['POSTGRES_ADDRESS'],
      database=os.environ['POSTGRES_DB'],
      user=os.environ['POSTGRES_USER'],
      password=os.environ['POSTGRES_PASSWORD']
    )
    self.cursor = self.connection.cursor()

  def query(self, query):
    try:
      self.cursor.execute(query)
      return self.cursor.fetchall()
    except Exception as err:
        print(err, file=sys.stderr)
        return None
    
  def query_with_params(self, query, param):
    try:
      self.cursor.execute(query, param)
      return self.cursor.fetchall()
    except Exception as err:
        print(err, file=sys.stderr)
        return None

  def commit(self):
    try:
      self.connection.commit()
    except Exception as err:
      self.connection.rollback()
      print("Error: commit failed", file=sys.stderr)

  def close(self):
    self.cursor.close()
    self.connection.close()