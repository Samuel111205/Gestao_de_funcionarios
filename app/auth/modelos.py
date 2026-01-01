from app.banco_de_dados import db

class Permissao(db.Model):
    __tablename__="permissoes"

    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(50), unique=True, nullable=False)


