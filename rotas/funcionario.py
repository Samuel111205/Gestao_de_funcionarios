from flask import Blueprint, render_template, request, redirect
from database.criar_tabelas import *

funcionario_route = Blueprint('funcionario', __name__)

# Página para cadastrar um novo funcionário
@funcionario_route.route('/funcionarios/novo')
def formulario_cadastro():
    return render_template("cadastro.html")
# Inserir funcionário no banco
@funcionario_route.route('/funcionarios', methods=['POST'])
def inserir_funcionario():

    nome = request.form["nome"].title()
    data_nascimento = request.form["data_nascimento"]
    genero = request.form["genero"]
    estado_civil = request.form["estado_civil"]
    email = request.form["email"]
    telefone = request.form["telefone"]

    #Redirecionando a rota inicial
    return redirect('/funcionarios')

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
