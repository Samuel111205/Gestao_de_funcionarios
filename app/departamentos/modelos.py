from app.banco_de_dados import db

class Departamentos(db.Model):
    __tablename__="departamentos"

    #Inserindo as colunas na tabela departamento
    id=db.Column(db.Integer, primary_key=True)
    nome_departamento=db.Column(db.String(120), unique=True, nullable=False, index=True)
    ativo=db.Column(db.Boolean, default=True)
    cargos=db.relationship("Cargos", back_populates="departamento", lazy=True)

    def __repr__(self):
        status="ativo" if self.ativo else "inativo"
        return f"<Departamento ({self.nome_departamento}) ({status})>"
