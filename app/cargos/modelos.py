from app.banco_de_dados import db

class Cargos(db.Model):
    __tablename__="cargos"
    # Inserindo as colunas na tabela Cargos
    id=db.Column(db.Integer, primary_key=True)
    nome_cargo=db.Column(db.String(120), nullable=False)
    departamento_id=db.Column(db.Integer, db.ForeignKey("departamentos.id", ondelete="CASCADE"), nullable=False)
    departamento=db.relationship("Departamentos", back_populates="cargos", lazy="joined")
    funcionarios=db.relationship("Funcionarios", back_populates="cargo", lazy="select", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Cargo id={self.id} nome={self.nome_cargo}>"
