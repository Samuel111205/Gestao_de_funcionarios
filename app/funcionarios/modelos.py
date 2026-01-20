from app.banco_de_dados import db
from datetime import date

class Funcionarios(db.Model):
    __tablename__="funcionarios"
    # Inserindo as colunas na tabela Funcionarios
    id=db.Column(db.Integer, primary_key=True)
    nome_funcionario=db.Column(db.String(120), nullable=False, index=True)
    data_nascimento=db.Column(db.Date, nullable=False)
    genero=db.Column(db.String(20), nullable=False)
    estado_civil=db.Column(db.String(40), nullable=False)
    email=db.Column(db.Text, unique=True, index=True)
    telefone=db.Column(db.Integer,nullable=False)
    data_admissao=db.Column(db.Date, default=date.today)

    cargo_id=db.Column(db.Integer, db.ForeignKey('cargos.id'), nullable=False)
    cargo=db.relationship("Cargos", back_populates="funcionarios", lazy=True)

    contratos=db.relationship("Contratos", back_populates="funcionario", lazy=True)
    ferias=db.relationship("Ferias", back_populates="funcionario", lazy=True)

    
    def statu_atual(self):
        hoje=date.today()
        
        if hasattr(self, "ferias"):
            for f in self.ferias:
                if f.ativa and f.data_inicio<= hoje <= f.data_fim:
                    return "Férias"
                
        for c in self.contratos:
            if c.ativo:
                return "Ativo"
        return "Encerrado"

    def __repr__(self):
        return f"<Funcionario id={self.id} nome={self.nome_funcionario}>"


class Ferias(db.Model):
    __tablename__="ferias"

    id=db.Column(db.Integer, primary_key=True)
    funcionario_id=db.Column(db.Integer, db.ForeignKey("funcionarios.id"))
    data_inicio=db.Column(db.Date, nullable=False)
    data_fim=db.Column(db.Date, nullable=False)
    ativa=db.Column(db.Boolean, default=True)
    funcionario=db.relationship("Funcionarios", back_populates="ferias")
