from app.banco_de_dados import db
from datetime import date, datetime

hora_de_entrada=datetime.now()
class Presencas(db.Model):
    __tablename__ = "presencas"

    id = db.Column(db.Integer, primary_key=True)
    contrato_id=db.Column(db.Integer, db.ForeignKey("contratos.id"), nullable=False)
    data=db.Column(db.Date, nullable=False, default=date.today)
    hora_entrada=db.Column(db.Date, nullable=False, default=datetime.now())
    hora_saida=db.Column(db.Date)

    status=db.Column(
        db.String(20),
        nullable=False,
        default="presente"
    )#presente| falta| justificativa| ferias
    observacao=db.Column(db.String(255))

    __table_args__=(
        db.UniqueConstraint(
            "contrato_id",
            "data",
            name="unique_presenca_por_dia"
        ),
    )

    def registrar_saida(self):
        self.hora_saida=datetime.now()

    def __repr__(self):
        return f"<Presenca {self.data} - {self.status}>"
