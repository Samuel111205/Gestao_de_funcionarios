import os
from app import criar_app
from app.banco_de_dados import db
from app.usuarios.modelos import Usuarios
from dotenv import load_dotenv

app=criar_app()
with app.app_context():
    load_dotenv()
    nome=os.getenv("NOME")
    email=os.getenv("EMAIL")
    perfil=os.getenv("PERFIL")
    senha=os.getenv("SENHA")

    admin=Usuarios(nome=nome, email=email, perfil=perfil)
    admin.set_senha(senha)
    db.session.add(admin)
    db.session.commit()

