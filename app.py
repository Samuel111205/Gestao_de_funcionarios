from flask import Flask
from database import db

def criar_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///funcionario.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)

    from rotas.home import home_route
    from rotas.funcionario import funcionario_route
    from rotas.departamento import departamento_route
    from rotas.cargos import cargo_route

    app.register_blueprint(home_route)
    app.register_blueprint(funcionario_route)
    app.register_blueprint(departamento_route)
    app.register_blueprint(cargo_route)

    return app

if __name__=="__main__":
    app=criar_app()
    app.run(debug=True)
