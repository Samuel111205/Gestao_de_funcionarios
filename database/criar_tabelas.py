from app import criar_app
from database import db
from modelos.departamentos import Departamentos
from modelos.cargos import Cargos
from modelos.funcionarios import Funcionarios
from modelos.presencas import Presencas
from modelos.contratos import Contratos
from modelos.salarios import Salarios

app=criar_app()

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso")
