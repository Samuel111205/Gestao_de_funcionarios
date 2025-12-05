from flask import render_template, request, redirect, url_for
from . import cargo_bp
from .modelos import Cargos
from app.banco_de_dados import db
from app.departamentos.modelos import Departamentos

@cargo_bp.route("/")
def listar_cargo():
    cargos=Cargos.query.all()
    return render_template("cargos/listar_cargos.html", cargos=cargos)

@cargo_bp.route("/cadastrar")
def cadastrar_cargo():
    departamentos=Departamentos.query.all()
    return render_template("cargos/cadastrar_cargos.html", departamentos=departamentos)

@cargo_bp.route("/inserir", methods=["POST"])
def inserir_departamento():
    return redirect(url_for("cargos.listar_cargos.html"))

@cargo_bp.route("/deletar/<int:id>", methods=["POST"])
def deletar_departamento(id):
    return redirect(url_for("cargos.listar_cargos"))
