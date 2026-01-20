from app.banco_de_dados import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth.tabelas import usuario_permissoes
from dotenv import load_dotenv
import os


load_dotenv()
perfil_admin=os.getenv("PERFIL_ADMIN")
perfil_usuario=os.getenv("PERFIL_USUARIO")
class Usuarios(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)  # mantém nome atual para evitar migração automática
    perfil = db.Column(db.String(20), default=perfil_usuario, nullable=False)
    ativo=db.Column(db.Boolean, default=True)
    permissoes = db.relationship(
        "Permissao",
        secondary=usuario_permissoes,
        backref=db.backref("usuarios", lazy="dynamic"),
        lazy="dynamic"  # permite consultas sem carregar todas as permissões
    )

    def __repr__(self):
        return f"<Usuario id={self.id} nome={self.nome!r} email={self.email!r} perfil={self.perfil!r}>"

    def set_senha(self, senha: str) -> None:
        """Armazena o hash da senha (lança erro para valor vazio)."""
        if not senha:
            raise ValueError("Senha não pode ser vazia")
        self.senha = generate_password_hash(senha)

    def check_senha(self, senha: str) -> bool:
        """Verifica a senha fornecida; retorna False se não houver hash armazenado."""
        if not self.senha:
            return False
        return check_password_hash(self.senha, senha)

    def is_admin(self) -> bool:
        """Retorna True se o perfil do usuário for administrador (comparação normalizada)."""
        return (self.perfil or "").strip().lower() == perfil_admin

    def tem_permissao(self, nome: str) -> bool:
        return self.permissoes.filter_by(nome=nome).first() is not None

