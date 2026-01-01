from flask import render_template, redirect, request, url_for
from flask_login import login_required
from . import contrato_bp
from .modelos import Contratos
from app.funcionarios.modelos import Funcionarios
from app.banco_de_dados import db
from datetime import date, datetime


@contrato_bp.route("/<int:funcionario_id>")
@login_required
def listar(funcionario_id):
    funcionario=Funcionarios.query.get_or_404(funcionario_id)
    return render_template("contratos/listar.html", funcionario=funcionario)


@contrato_bp.route("/inserir/<int:funcionario_id>", methods=["POST"])
@login_required
def inserir(funcionario_id):
    tipo=request.form.get("tipo").title()
    salario_base=request.form.get("salario_base")
    data_inicio=datetime.strptime(request.form.get("data_inicio"), "%Y-%m-%d").date()
    data_fim=datetime.strptime(request.form.get("data_fim"), "%Y-%m-%d").date()

    contrato=Contratos(
        funcionario_id=funcionario_id,
        tipo=tipo,
        salario_base=salario_base,
        data_inicio=data_inicio,
        data_fim=data_fim
    )
    db.session.add(contrato)
    db.session.commit()
    return redirect(url_for("contrato.listar", funcionario_id=funcionario_id))
