from flask import render_template, request, redirect, url_for, flash
from . import cargo_bp
from .modelos import Cargos
from app.banco_de_dados import db
from app.departamentos.modelos import Departamentos
from flask_login import login_required
from app.auth.permissoes import permissao_requerida


# Rota que Lista todos os cargos e os seus departamentos
@cargo_bp.route("/")
@login_required
def listar_cargo():
    page=request.args.get('page',1,type=int)
    cargos=Cargos.query.join(Departamentos).order_by(
        Departamentos.nome_departamento,
        Cargos.nome_cargo
    ).all()
    return render_template("cargos/listar_cargos.html", cargos=cargos)

#Rota que  faz o cadastrando de cargos
@cargo_bp.route("/cadastrar")
@login_required
def cadastrar_cargo():
    departamentos=Departamentos.query.filter_by(ativo=True).order_by(Departamentos.nome_departamento).all()
    return render_template("cargos/cadastrar_cargos.html", departamentos=departamentos)

#Rota que recebe as informações do formulario e cadastra no banco de dados
@cargo_bp.route("/inserir", methods=["POST"])
@login_required
def inserir_cargo():
    nome_cargo=request.form.get("nome_cargo").strip().title()
    departamento_id=request.form.get("departamento_id")

    if not nome_cargo or not departamento_id:
        flash("Todos os campos são obrigatorios.", "erro")
        return redirect(url_for("cargos.cadastrar_cargo"))

    #Evitar duplicados (no mesmo departamento)
    if Cargos.query.filter_by(nome_cargo=nome_cargo,departamento_id=departamento_id).first():
        flash("Cargo ja existente", "erro")
        return redirect(url_for("cargos.cadastrar_cargo"))

    cargo=Cargos(nome_cargo=nome_cargo,departamento_id=departamento_id)
    db.session.add(cargo)
    db.session.commit()
    flash("Cargo cadastrado com sucesso", "sucesso")
    return redirect(url_for("cargos.listar_cargo"))


@cargo_bp.route("/<int:cargo_id>/ativar")
@login_required
def ativar_cargo(cargo_id):
    cargo=Cargos.query.get_or_404(cargo_id)
    cargo.ativo=True
    db.session.commit()
    flash("Cargo ativado com sucesso", "sucesso")
    return redirect(url_for("cargos.listar_cargo"))

@cargo_bp.route("/<int:cargo_id>/desativar")
@login_required
def desativar_cargo(cargo_id):
    cargo=Cargos.query.get_or_404(cargo_id)
    cargo.ativo=False
    db.session.commit()
    flash("Cargo desativado com sucesso", "sucesso")
    return redirect(url_for("cargos.listar_cargo"))
