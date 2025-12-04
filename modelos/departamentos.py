from database import db
from app import criar_app

#Tabbela departamento
class Departamentos(db.Model):
    #Inserindo as colunas na tabela departamento
    id=db.Column(db.Integer, primary_key=True)
    nome_departamento=db.Column(db.String(120), unique=True, nullable=False)
    cargos=db.relationship("cargos", backref="departamento", lazy=True)
app=criar_app()

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso")
