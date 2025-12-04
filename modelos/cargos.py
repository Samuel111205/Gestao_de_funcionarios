from database import db

class Cargos(db.Model):
    # Inserindo as colunas na tabela Cargos
    id=db.Column(db.Integer, primary_key=True)
    nome_cargo=db.Column(db.String(120), nullable=False)
    departamento_id=db.Column(db.Integer, db.ForeignKey("departamento.id"))
