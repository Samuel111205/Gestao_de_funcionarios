from app.banco_de_dados import db


class Salarios(db.Model):
    __tablename__="salarios"
    id=db.Column(db.Integer, primary_key=True)
    contrato_id=db.Column(db.Integer, db.ForeignKey("contratos.id"), nullable=False)
    mes=db.Column(db.Integer, nullable=False)
    ano=db.Column(db.Integer, nullable=False)
    faltas=db.Column(db.Integer, default=0)
    dias_trabalhadas=db.Column(db.Integer, default=0)
    descontos=db.Column(db.Float, default=0)
    acrescimos=db.Column(db.Float, default=0)
    salario_base=db.Column(db.Float, nullable=False)
    valor_final=db.Column(db.Float, nullable=False)
    contrato=db.relationship("Contratos", back_populates="salarios")

    __table_args__=(db.UniqueConstraint("contrato_id", "mes", "ano"),)
