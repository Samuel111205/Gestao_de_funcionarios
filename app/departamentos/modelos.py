from app.banco_de_dados import db

class Departamentos(db.Model):
    __tablename__="departamentos"

    #Inserindo as colunas na tabela departamento
    id=db.Column(db.Integer, primary_key=True)
    nome_departamento=db.Column(db.String(120), unique=True, nullable=False)
    cargos=db.relationship("Cargos", back_populates="departamento", lazy="select", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Departamento id={self.id} nome={self.nome_departamento}>"


