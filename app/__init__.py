from flask import Flask
from .banco_de_dados import db
from flask_login import LoginManager


login_maneger=LoginManager()
login_maneger.login_view="auth.login"
def criar_app(test_config=None):
    app=Flask(__name__, template_folder="../templates", instance_relative_config=False)
    #Configurações principais
    app.config.from_mapping(SECRET_KEY="dev-key", SQLALCHEMY_DATABASE_URI="sqlite:///funcionario.db", SQLALCHEMY_TRACK_MODIFICATIONS=False)
    if test_config:
        app.config.update(test_config)
    #Inicializar o banco
    db.init_app(app)
    login_maneger.init_app(app)

    from .usuarios.modelos import Usuarios

    @login_maneger.user_loader
    def loader_user(user_id):
        return Usuarios.query.get(int(user_id))

    from .departamentos import departamento_bp
    from .cargos import cargo_bp
    from .funcionarios import funcionario_bp
    from .home import home_bp
    from .salarios import salario_bp
    from .auth import auth_bp
    from .categorias import categoria_bp
    from .contratos import contrato_bp
    from .presencas import presenca_bp

    #Registrar rotas(Blueprints)
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(departamento_bp, url_prefix="/departamentos")
    app.register_blueprint(cargo_bp, url_prefix="/cargos")
    app.register_blueprint(funcionario_bp, url_prefix="/funcionarios")
    app.register_blueprint(salario_bp, url_prefix="/salarios")
    app.register_blueprint(categoria_bp, url_prefix="/categorias")
    app.register_blueprint(contrato_bp, url_prefix="/contratos")
    app.register_blueprint(presenca_bp, url_prefix="/presencas")

    with app.app_context():
        db.create_all()
    return app
