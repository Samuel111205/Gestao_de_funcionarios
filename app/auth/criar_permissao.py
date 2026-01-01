from modelos import Permissao
from app.banco_de_dados import db
from app import criar_app
app=criar_app()
with app.app_context():
    permissoes=[
        "criar_funcionario",
        "editar_funcionario",
        "excluir_funcionario",
        "calcular_salario",
        "gerir_contratos",
        "geiri_permissoes"
    ]
    for nome in permissoes:
        if not Permissao.query.filter_by(nome=nome).first():
            db.session.add(Permissao(nome=nome))
    print("Premissoes adicionadas com sucesso")
    db.session.commit()

