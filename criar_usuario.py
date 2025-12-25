from app import criar_app
from app.banco_de_dados import db
from app.usuarios.modelos import Usuarios

app=criar_app()
with app.app_context():
    admin=Usuarios(nome="Samuel", email="samuel@gmail.com", perfil="administrador")
    admin.set_senha("111205")
    db.session.add(admin)
    db.session.commit()

