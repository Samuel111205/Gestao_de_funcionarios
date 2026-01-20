from app.banco_de_dados import db

class Cargos(db.Model):
    __tablename__="cargos"
    # Inserindo as colunas na tabela Cargos
    id=db.Column(db.Integer, primary_key=True)
    nome_cargo=db.Column(db.String(120), nullable=False, index=True)
    ativo=db.Column(db.Boolean, default=True)
    departamento_id=db.Column(db.Integer, db.ForeignKey("departamentos.id"), nullable=False)
    departamento=db.relationship("Departamentos", back_populates="cargos", lazy="joined")
    funcionarios=db.relationship("Funcionarios", back_populates="cargo", lazy=True)

    def __repr__(self):
        status="ativo" if self.ativo else "inativo"
        return f"<Cargo ({self.nome_cargo}) ({status})>"
