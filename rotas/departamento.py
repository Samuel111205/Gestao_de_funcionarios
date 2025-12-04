from flask import Blueprint, request, render_template,redirect,url_for
from modelos.departamentos import Departamentos
from database import db

departamento_route=Blueprint('departamento', __name__,url_prefix="/departamento")



#Inserir o departamento
@departamento_route.route('/departamento', methods=['GET','POST'])
def inserir_departamento():
    if request.method=="POST":
        nome_departamento=request.form["nome_departamento"]
        departamento=Departamentos(nome_departamento=nome_departamento)
        db.session.add(departamento)
        db.session.commit()
        return redirect(url_for( "departamento.listar"))

    return render_template("cadastrar_departamento.html")

# Listar Departamento
@departamento_route.route('/funcionarios')
def listar_departamento():
    pass

# Deletar Departamento
@departamento_route.route('/departamento/<int:departamento_id>/deletar', methods=['POST'])
def deletar_departamento(departamento_id):
    pass
