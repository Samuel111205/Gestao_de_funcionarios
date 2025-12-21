from flask import render_template, request, redirect, url_for, flash
from . import cargo_bp
from .modelos import Cargos
from app.banco_de_dados import db
from app.departamentos.modelos import Departamentos

# Rota que Lista todos os cargos e os seus departamentos
@cargo_bp.route("/")
def listar_cargo():
    page=request.args.get('page',1,type=int)
    cargos=Cargos.query.order_by(Cargos.nome_cargo).paginate(page=page, per_page=10)
    return render_template("cargos/listar_cargos.html", cargos=cargos)

#Rota que  faz o cadastrando de cargos
@cargo_bp.route("/cadastrar")
def cadastrar_cargo():
    departamentos=Departamentos.query.order_by(Departamentos.nome_departamento).all()
    return render_template("cargos/cadastrar_cargos.html", departamentos=departamentos)

#Rota que recebe as informações do formulario e cadastra no banco de dados
@cargo_bp.route("/inserir", methods=["POST"])
def inserir_cargo():
    nome_cargo=request.form.get("nome_cargo").title()
    departamento_id=request.form.get("departamento_id")

    if not nome_cargo or not departamento_id:

        return "Preencha todos os campos", 400

    #Verificar se departamento existe
    departamento=Departamentos.query.get(departamento_id)
    if not departamento:
        return "Departamento não encotrado", 400

    #Evitar duplicados (no mesmo departamento)
    if Cargos.query.filter_by(nome_cargo=nome_cargo,departamento_id=departamento_id).first():
        return "Cargo ja existe nesse departamento", 400

    flash("Cargo cadastrado com sucesso")
    cargo=Cargos(nome_cargo=nome_cargo,departamento_id=departamento_id)
    db.session.add(cargo)
    db.session.commit()
    return redirect(url_for("cargos.listar_cargo"))

#Rota que deleta um cargo no banco de dados
@cargo_bp.route("/deletar/<int:cargo_id>", methods=["POST"])
def deletar_cargo(cargo_id):
    cargo=Cargos.query.get_or_404(cargo_id)
    db.session.delete(cargo)
    db.session.commit()
    return redirect(url_for("cargos.listar_cargo"))
