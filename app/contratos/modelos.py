from app.banco_de_dados import db

class Contratos(db.Model):
    __tablename__="contratos"

    id=db.Column(db.Integer, primary_key=True)
    funcionario_id=db.Column(db.Integer, db.ForeignKey("funcionarios.id"), nullable=False)
    tipo=db.Column(db.String(50), nullable=False)
    salario_base=db.Column(db.Float, nullable=False)
    data_inicio=db.Column(db.Date, nullable=False)
    data_fim=db.Column(db.Date, nullable=True)
    ativo=db.Column(db.Boolean, default=True)
    funcionario=db.relationship("Funcionarios", back_populates="contratos")
    salarios=db.relationship("Salarios", back_populates="contrato")

    def __repr__(self):
        return f"<Contrato id={self.id} funcionario_id={self.funcionario_id}>"
