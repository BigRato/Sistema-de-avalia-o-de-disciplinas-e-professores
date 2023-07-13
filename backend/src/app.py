from flask import Flask
from flask_cors import CORS

from .database import Database

from .controllers.EstudanteController import EstudanteController
from .controllers.ProfessorController import ProfessorController
from .controllers.AvaliacaoTurmaController import AvaliacaoTurmaController
from .controllers.AvaliacaoProfessorController import AvaliacaoProfessorController
from .controllers.DenunciaAvaliacaoTurmaController import DenunciaAvaliacaoTurmaController
from .controllers.DenunciaAvaliacaoProfessorController import DenunciaAvaliacaoProfessorController
from .controllers.LoginController import LoginController

app = Flask(__name__)
CORS(app)

database = Database()

estudante_controller = EstudanteController(app, database)
professor_controller = ProfessorController(app, database)
avaliacao_turma_controller = AvaliacaoTurmaController(app, database)
avaliacao_professor_controller = AvaliacaoProfessorController(app, database)
denuncia_avaliacao_turma_controller = DenunciaAvaliacaoTurmaController(app, database)
denuncia_avaliacao_professor_controller = DenunciaAvaliacaoProfessorController(app, database)
login_controller = LoginController(app, database)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)