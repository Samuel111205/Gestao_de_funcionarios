from app.banco_de_dados import db
from datetime import date

class Salarios(db.Model):
    __tablename__="salarios"
    id=db.Column(db.Integer, primary_key=True)
    contrato_id=db.Column(db.Integer, db.ForeignKey("contratos.id"), nullable=False)
    valor=db.Column(db.Float, nullable=False)
    data_inicio=db.Column(db.Date, nullable=False, default=date.today)
    data_fim=db.Column(db.Date)
    ativo=db.Column(db.Boolean, default=True)
    contrato=db.relationship("Contratos", back_populates="salarios", lazy=True)

    def encerrar(self, data_encerramento=None):
        self.ativo=False
        self.data_fim=data_encerramento or date.today()

    def __repr__(self):
        status="ativo" if self.ativo else "encerrado"
        return f"<Salario {self.valor} ({status})"
