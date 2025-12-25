from app.banco_de_dados import db
from datetime import date
class Salarios(db.Model):
    __tablename__="salarios"
    salario_id=db.Column(db.Integer, primary_key=True)
    valor=db.Column(db.Float, nullable=False)
    data_inicio=db.Column(db.Date, nullable=False, default=date.today)
    funcionario_id=db.Column(db.Integer, db.ForeignKey("funcionarios.id"), nullable=False)
