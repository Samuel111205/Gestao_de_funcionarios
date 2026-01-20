from flask import render_template, Blueprint, request
from flask_login import login_required
from app.funcionarios.modelos import Funcionarios, Ferias
from app.banco_de_dados import db
from app.contratos.modelos import Contratos

home_bp=Blueprint("home",__name__)

@home_bp.route("/")
def conteudo():
    return render_template("conteudo.html")

@home_bp.route("/home")
def home():
    return render_template("home.html")

@home_bp.route("/dashboard")
@login_required
def dashboard():
    total_funcionarios = Funcionarios.query.count()
    ativos = Contratos.query.order_by(Contratos.ativo=="Ativos").count()
    ferias = Ferias.query.filter_by(ativa=True).count()
    novos_contratos = Contratos.query.count()
    funcionarios = Funcionarios.query.limit(5).all()

    return render_template(
        "dashboard.html",
        total_funcionarios=total_funcionarios,
        ativos=ativos,
        ferias=ferias,
        novos_contratos=novos_contratos,
        funcionarios=funcionarios
    )

