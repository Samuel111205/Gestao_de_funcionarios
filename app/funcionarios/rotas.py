from flask import render_template, request, redirect, url_for
from . import funcionario_bp
from .modelos import Funcionarios
from app.banco_de_dados import db
from app.cargos.modelos import Cargos

@funcionario_bp.route("/")
def listar_funcionarios():
    funcionarios=Funcionarios.query.all()
    return render_template("funcionarios/listar_funcionarios.html", funcionarios=funcionarios)

@funcionario_bp.route("/cadastrar")
def cadastrar_funcionario():
    cargos=Cargos.query.all()
    return render_template("funcionarios/cadastrar_funcionarios.html", cargos=cargos)

@funcionario_bp.route("/inserir", methods=["POST"])
def inserir_funcionario():
    return redirect(url_for("funcionario.listar_funcionarios"))

@funcionario_bp.route("/editar/<int:id>")
def editar_funcionario(id):
    funcionario=Funcionarios.query.get(id)
    cargos=Cargos.query.all()
    return render_template("funcionario/editar_funcionarios.html")

@funcionario_bp.route("/atualizar/<int:id>", methods=["POST"])
def atualizar_funcionario(id):
    return redirect(url_for("funcionario.listar_funcionarios"))

@funcionario_bp.route("/deletar/<int:id>", methods=["POST"])
def deletar_funcionario(id):
    return redirect(url_for("funcionario.listar_funcionarios"))
