from flask import Blueprint, request, render_template, redirect, url_for
from . import departamento_bp
from .modelos import Departamentos
from app.banco_de_dados import db

@departamento_bp.route("/")
def listar_departamento():
    page=request.args.get('page',1, type=int)
    departamentos=Departamentos.query.order_by(Departamentos.nome_departamento).paginate(page=page, per_page=10)
    return render_template("departamentos/lista_departamentos.html", departamentos=departamentos)

@departamento_bp.route("/cadastrar")
def cadastrar_departamentos():
    return render_template("departamentos/cadastrar_departamentos.html")

@departamento_bp.route("/inserir", methods=["POST"])
def inserir_departamento():
    nome_departamento=request.form.get("nome_departamento").strip().title()
    if not nome_departamento:
        return "Preencha o nome do departamento",400
    if Departamentos.query.filter_by(nome_departamento=nome_departamento).first():
        return "Departamento ja existe"

    departamento=Departamentos(nome_departamento=nome_departamento)
    db.session.add(departamento)
    db.session.commit()
    return redirect(url_for("departamento.listar_departamento"))

@departamento_bp.route("/deletar/<int:departamento_id>", methods=["POST"])
def deletar_departamento(departamento_id):
    departamento=Departamentos.query.get_or_404(departamento_id)
    db.session.delete(departamento)
    db.session.commit()
    return redirect(url_for("departamento.listar_departamento"))
