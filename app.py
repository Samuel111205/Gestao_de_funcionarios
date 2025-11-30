from flask import *
from rotas.home import home_route
from rotas.funcionario import funcionario_route
from rotas.departamento import departamento_route
from rotas.cargos import cargo_route

app=Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(funcionario_route)
app.register_blueprint(departamento_route)
app.register_blueprint(cargo_route)

if __name__=="__main__":
    app.run(debug=True)
