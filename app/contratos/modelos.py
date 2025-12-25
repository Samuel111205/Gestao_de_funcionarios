from app.banco_de_dados import db

class Contratos(db.Model):
    __tablename__="contratos"

    id=db.Column(db.Integer, primary_key=True)
    funcionario_id=db.Column(db.Integer, db.ForeignKey("funcionarios.id"), nullable=False)
    categoria_id=db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    data_inicio=db.Column(db.Date, nullable=False)
    data_fim=db.Column(db.Date, nullable=True)
    ativo=db.Column(db.Boolean, default=False)
    funcionario=db.relationship("Funcionarios", back_populates="contratos")
    categorias=db.relationship("Categorias", back_populates="contratos")

    def __repr__(self):
        return f"<Contrato id={self.id} funcionario_id={self.funcionario_id}>"
