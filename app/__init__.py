import os
from flask import Flask
from .banco_de_dados import db
from flask_login import LoginManager
from dotenv import load_dotenv


load_dotenv()
login_maneger=LoginManager()
login_maneger.login_view="usuarios.login"
def criar_app(test_config=None):
    chave_secreta=os.getenv("CHAVE_SECRETA")
    database_uri=os.getenv("DATABASE_URI")
    app=Flask(__name__, template_folder="../templates", instance_relative_config=False)
    #Configurações principais
    app.config.from_mapping(SECRET_KEY=chave_secreta, SQLALCHEMY_DATABASE_URI=database_uri, SQLALCHEMY_TRACK_MODIFICATIONS=False)
    if test_config:
        app.config.update(test_config)
    #Inicializar o banco
    db.init_app(app)
    login_maneger.init_app(app)
    login_maneger.login_view="usuarios.login"

    from .usuarios.modelos import Usuarios

    @login_maneger.user_loader
    def loader_user(user_id):
        return Usuarios.query.get(int(user_id))

    from .departamentos import departamento_bp
    from .cargos import cargo_bp
    from .funcionarios import funcionario_bp
    from .home import home_bp
    from .salarios import salario_bp
    from .contratos import contrato_bp
    from .presencas import presenca_bp
    from .usuarios import usuario_bp

    #Registrar rotas(Blueprints)
    app.register_blueprint(home_bp)
    app.register_blueprint(departamento_bp, url_prefix="/departamentos")
    app.register_blueprint(cargo_bp, url_prefix="/cargos")
    app.register_blueprint(funcionario_bp, url_prefix="/funcionarios")
    app.register_blueprint(usuario_bp, url_prefix="/usuarios")
    app.register_blueprint(salario_bp, url_prefix="/salarios")
    app.register_blueprint(contrato_bp, url_prefix="/contratos")
    app.register_blueprint(presenca_bp, url_prefix="/presencas")

    with app.app_context():
        from app.departamentos import modelos
        from app.cargos import modelos
        from app.funcionarios import modelos
        from app.contratos import modelos
        from app.salarios import modelos
        from app.presencas import modelos
        from app.auth import modelos
        from app.auth import tabelas
        from app.usuarios import modelos

        db.create_all()
    return app
