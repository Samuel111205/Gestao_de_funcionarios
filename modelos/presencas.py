from database import db

#Tabbela Presenças
class Presencas(db.Model):
    # Inserindo as colunas na tabela Presenças
    presenca_id=db.Column(db.Integer, primary_key=True)
    funcionario_id=db.Column(db.Integer, db.ForeignKey('funcionarios.id'), nullable=False)
    data=db.Column(db.Date, nullable=False)
    presente=db.Column(db.Boolean, nullable=False)
