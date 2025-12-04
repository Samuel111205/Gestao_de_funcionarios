from database import db

#Tabbela Contratos
class Contratos(db.Model):
    # Inserindo as colunas na Contratos
    licenca_id=db.Column(db.Integer, primary_key=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'), nullable=False)
    tipo_licenca=db.Column(db.Text, nullable=False)
    data_inicio=db.Column(db.Date, nullable=False)
    data_fim=db.Column(db.Date, nullable=False)
    estado=db.Column(db.Text, nullable=False)