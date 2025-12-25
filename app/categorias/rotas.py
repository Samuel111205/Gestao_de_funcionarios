from flask import render_template, request, redirect, url_for
from flask_login import login_required
from . import categoria_bp
from .modelos import Categorias
from app.banco_de_dados import db

@categoria_bp.route("/")
@login_required
def listar():
    categorias=Categorias.query.order_by(Categorias.nome).all()
    return render_template("categorias/listar.html", categorias=categorias)

@categoria_bp.route("/cadastrar")
@login_required
def cadastrar():
    return render_template("categorias/cadastrar.html")

@categoria_bp.route("/inserir", methods=["POST"])
@login_required
def inserir():
    nome=request.form.get("nome")
    categoria=Categorias(nome=nome)
    db.session.add(categoria)
    db.session.commit()
    return redirect(url_for("categoria.listar"))

