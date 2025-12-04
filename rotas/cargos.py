from flask import Blueprint, request, render_template,redirect


cargo_route=Blueprint('cargos', __name__)

#Rota para cadastrar o departamento
@cargo_route.route('/cargos/novo')
def cadastrar_departamento():
    pass
#Inserir o departamento
@cargo_route.route('/cargos', methods=['POST'])
def inserir_departamento():
    pass

# Listar Departamento
@cargo_route.route('/cargos')
def listar_departamento():
    pass

# Deletar Departamento
@cargo_route.route('/cargos/<int:cargo_id>/deletar', methods=['POST'])
def deletar_departamento(departamento_id):
    pass