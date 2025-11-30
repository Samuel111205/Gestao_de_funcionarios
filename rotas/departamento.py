from flask import Blueprint, request, render_template,redirect
from database.banco_de_daos import conectar
from database.criar_tabelas import criar_tabela

departamento_route=Blueprint('departamento', __name__)

#Rota para cadastrar o departamento
@departamento_route.route('/departamento/novo')
def cadastrar_departamento():
    pass
#Inserir o departamento
@departamento_route.route('/departamento', methods=['POST'])
def inserir_departamento():
    pass

# Listar Departamento
@departamento_route.route('/funcionarios')
def listar_departamento():
    pass

# Deletar Departamento
@departamento_route.route('/departamento/<int:departamento_id>/deletar', methods=['POST'])
def deletar_departamento(departamento_id):
    pass
