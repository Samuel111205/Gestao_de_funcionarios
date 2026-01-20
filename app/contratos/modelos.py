from app.banco_de_dados import db
from datetime import date

class Contratos(db.Model):
    __tablename__="contratos"

    id=db.Column(db.Integer, primary_key=True)
    funcionario_id=db.Column(db.Integer, db.ForeignKey("funcionarios.id"), nullable=False)
    tipo=db.Column(db.String(50))
    data_inicio=db.Column(db.Date, nullable=False, default=date.today)
    data_fim=db.Column(db.Date)
    ativo=db.Column(db.Boolean, default=True)
    funcionario=db.relationship("Funcionarios", back_populates="contratos")
    salarios=db.relationship("Salarios", back_populates="contrato", lazy=True)

    def encerrar(self, data_encerramento=None):
        self.ativo=False
        self.data_fim=data_encerramento or date.today()
    def __repr__(self):
        status="ativo" if self.ativo else "encerrado"
        return f"<Contrato ({self.id}) ({status})>"
