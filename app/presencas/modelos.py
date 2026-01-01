from app.banco_de_dados import db
from datetime import date

class Presencas(db.Model):
    __tablename__ = "presencas"

    id = db.Column(db.Integer, primary_key=True)

    funcionario_id = db.Column(
        db.Integer,
        db.ForeignKey("funcionarios.id"),
        nullable=False
    )

    data = db.Column(db.Date, default=date.today, nullable=False)

    presente = db.Column(db.Boolean, default=True)

    funcionario = db.relationship(
        "Funcionarios",
        back_populates="presencas"
    )

    def __repr__(self):
        return f"<Presenca funcionario_id={self.funcionario_id} data={self.data}>"
