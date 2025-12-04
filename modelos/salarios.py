from database import db

#Tabbela salarios
class Salarios(db.Model):
    # Inserindo as colunas na tabela salarios
    salario_id=db.Column(db.Integer, primary_key=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.funcionario_id'), nullable=False)
    salario_diario=db.Column(db.Float)
    salario_mensal=db.Column(db.Float)
    salario_descontado=db.Column(db.Float)