from flask import Flask
from .banco_de_dados import db
from .departamentos import departamento_bp
from .cargos import cargo_bp
from .funcionarios import funcionario_bp
from .home import home_bp

def criar_app(test_config=None):
    app=Flask(__name__, template_folder="../templates", instance_relative_config=False)
    #Configurações principais
    app.config.from_mapping(SECRET_KEY="dev-key", SQLALCHEMY_DATABASE_URI="sqlite:///funcionario.db", SQLALCHEMY_TRACK_MODIFICATIONS=False)
    if test_config:
        app.config.update(test_config)
    #Inicializar o banco
    db.init_app(app)
    #Registrar rotas(Blueprints)
    app.register_blueprint(home_bp)
    app.register_blueprint(departamento_bp, url_prefix="/departamentos")
    app.register_blueprint(cargo_bp, url_prefix="/cargos")
    app.register_blueprint(funcionario_bp, url_prefix="/funcionarios")

    with app.app_context():
        db.create_all()
    return app
