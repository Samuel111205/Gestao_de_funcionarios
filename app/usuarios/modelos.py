from app.banco_de_dados import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


usuario_permissoes=db.Table(
    "usuario_permissoes",
    db.Column("usuario_id", db.Integer, db.ForeignKey("usuarios.id")),
    db.Column("permissao_id", db.Integer, db.ForeignKey("permissoes.id"))
)
class Usuarios(UserMixin,db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    perfil=db.Column(db.String(20), default="usuario")#valores: "adiministrador"| "Usuario"
    permissoes=db.relationship("Permissao", secondary=usuario_permissoes, backref="usuarios")

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)

    def is_admin(self):
        return self.perfil=="Administrador"

    def tem_permissao(self, nome):
        return any(p.nome==nome for p in self.permissoes)
