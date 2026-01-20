from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required
from . import salario_bp
from .modelos import Salarios
from app.contratos.modelos import Contratos
from app.banco_de_dados import db
from datetime import datetime
from app.auth.permissoes import permissao_requerida


@salario_bp.route("/contrato/<int:contrato_id>")
@login_required
def listar_salarios(contrato_id):
    contrato=Contratos.query.get_or_404(contrato_id)
    salarios=Salarios.query.filter_by(
        contrato_id=contrato.id,
    ).order_by(Salarios.data_inicio.desc()).all()
    return render_template("salarios/listar.html", contrato=contrato, salarios=salarios)


@salario_bp.route("/criar/<int:contrato_id>", methods=["GET","POST"])
@login_required
@permissao_requerida("administrador")
def criar_salario(contrato_id):
    contrato=Contratos.query.get_or_404(contrato_id)
    salario_ativo=Salarios.query.filter_by(
        contrato_id=contrato.id,
        ativo=True
    ).first()
    if request.method=="POT":
        valor=float(request.form.get("valor"))
        data_inicio=datetime.strptime(request.form.get("data_inicio"), "%Y-%m-%d").date()
        if salario_ativo:
            salario_ativo.encerrar()
        novo_salario=Salarios(
            contrato_id=contrato.id,
            valor=valor,
            data_inicio=data_inicio
        )
        db.session.add(novo_salario)
        db.session.commit()
        flash("Salario registrado com sucesso.", "sucesso")
        return redirect(url_for("salario.listar_salarios", contrato_id=contrato.id))
    return render_template("salarios/criar_salarios.html", contrato=contrato, salario_ativo=salario_ativo)

