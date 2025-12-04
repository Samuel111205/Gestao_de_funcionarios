from database import db

#Tabbela Funcionarios
class Funcionarios(db.Model):
    # Inserindo as colunas na tabela Funcionarios
    id=db.Column(db.Integer, primary_key=True)
    nome_funcionario=db.Column(db.String(120), nullable=False)
    data_nascimento=db.Column(db.Date, nullable=False)
    genero=db.Column(db.String(20), nullable=False)
    estado_civil=db.Column(db.String(40), nullable=False)
    email=db.Column(db.Text, unique=True, nullable=False)
    telefone=db.Column(db.Integer,nullable=False)
    cargo_id=db.Column(db.Integer, db.ForeignKey('cargos.id'))
