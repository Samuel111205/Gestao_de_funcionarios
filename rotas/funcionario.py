from flask import Blueprint, render_template, request, redirect, url_for
from modelos.cargos import Cargos
from modelos.funcionarios import Funcionarios
from database import db


funcionario_route = Blueprint('funcionario', __name__,url_prefix="/funcionario")

@funcionario_route.route('/funcionarios', methods=['GET','POST'])
def inserir_funcionario():
    #cargo=Cargos.query.all()

    if request.method=="POST":
        nome = request.form.get("nome").title()
        data_nascimento = request.form.get("data_nascimento")
        genero = request.form.get("genero")
        estado_civil = request.form.get("estado_civil")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        cargo_id=request.form.get("cargo_id")

        funcionario=Funcionarios(nome=nome,data_nascimento=data_nascimento,genero=genero,estado_civil=estado_civil,email=email,telefone=telefone,cargo_id=cargo_id)
        db.session.add(funcionario)
        db.session.commit()
        #Redirecionando a rota inicial
        return redirect(url_for("funcionario.listar"))

    return render_template("cadastro.html")

# Listar funcionários
@funcionario_route.route('/funcionarios')
def listar_funcionarios():
    return render_template("lista.html")

# Formulário para editar funcionário
@funcionario_route.route('/funcionarios/<int:funcionario_id>/editar')
def editar_funcionario(funcionario_id):

    return render_template("editar_funcionario.html")

# Atualizar funcionário
@funcionario_route.route('/funcionarios/<int:funcionario_id>/atualizar', methods=['POST'])
def atualizar_funcionario(funcionario_id):
    nome = request.form['nome'].title()
    estado_civil = request.form['estado_civil']
    email = request.form['email']
    telefone = request.form['telefone']

    return redirect('/funcionarios')

# Deletar funcionário
@funcionario_route.route('/funcionarios/<int:funcionario_id>/deletar', methods=['POST'])
def deletar_funcionario(funcionario_id):


    return redirect('/funcionarios')
