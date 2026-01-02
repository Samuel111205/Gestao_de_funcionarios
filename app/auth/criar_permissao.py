from modelos import Permissao
from app.banco_de_dados import db
from app import criar_app

def adicionar_permissoes():
    app = criar_app()
    permissoes = [
        "criar_funcionario",
        "editar_funcionario",
        "excluir_funcionario",
        "calcular_salario",
        "gerir_contratos",
        "gerir_permissoes"
    ]

    with app.app_context():
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

