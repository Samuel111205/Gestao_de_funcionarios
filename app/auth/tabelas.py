from app.banco_de_dados import db


usuario_permissoes=db.Table(
    "usuario_permissoes",
    db.Column("usuario_id", db.Integer, db.ForeignKey("usuarios.id")),
    db.Column("permissao_id", db.Integer, db.ForeignKey("permissao.id"))
)
