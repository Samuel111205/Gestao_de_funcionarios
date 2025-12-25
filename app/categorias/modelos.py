from app.banco_de_dados import db

class Categorias(db.Model):
    __tablename__="categorias"
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(50), nullable=False, unique=True)

