from app.banco_de_dados import db

class Funcionarios(db.Model):
    __tablename__="funcionarios"
    # Inserindo as colunas na tabela Funcionarios
    id=db.Column(db.Integer, primary_key=True)
    nome_funcionario=db.Column(db.String(120), nullable=False)
    data_nascimento=db.Column(db.Date, nullable=False)
    genero=db.Column(db.String(20), nullable=False)
    estado_civil=db.Column(db.String(40), nullable=False)
    email=db.Column(db.Text, unique=True, nullable=False)
    telefone=db.Column(db.Integer,nullable=False)

    cargo_id=db.Column(db.Integer, db.ForeignKey('cargos.id', ondelete="SET NULL"), nullable=False)
    cargo=db.relationship("Cargos", back_populates="funcionarios", lazy="joined")

    categoria_id=db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=False)
    categorias=db.relationship("Categorias")

    salarios = db.relationship("Salarios", backref="funcionario", lazy=True,
                                   cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Funcionario id={self.id} nome={self.nome_funcionario}>"
