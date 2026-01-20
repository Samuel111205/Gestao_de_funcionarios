import os
from app import criar_app
from app.banco_de_dados import db
from app.usuarios.modelos import Usuarios
from app.auth.modelos import Permissao
from dotenv import load_dotenv


def adicionar_permissoes():
    app = criar_app()
    permissoes = [
        "criar_funcionario",
        "editar_funcionario",
        "excluir_funcionario",
        "calcular_salario",
        "gerir_contratos",
        "gerir_permissoes",
        "gerir_usuarios"
    ]

    with app.app_context():
        load_dotenv()
        nome = os.getenv("NOME")
        email = os.getenv("EMAIL")
        perfil = os.getenv("PERFIL")
        senha = os.getenv("SENHA")

        admin = Usuarios(nome=nome, email=email, perfil=perfil)
        admin.set_senha(senha)
        db.session.add(admin)
        db.session.commit()
        try:
            for nome in permissoes:
                if not Permissao.query.filter_by(nome=nome).first():
                    db.session.add(Permissao(nome=nome))
            db.session.commit()
            print("Permissões adicionadas com sucesso")
        except Exception as e:
            db.session.rollback()
            print("Erro ao adicionar permissões:", e)
            raise

if __name__ == "__main__":
    adicionar_permissoes()

