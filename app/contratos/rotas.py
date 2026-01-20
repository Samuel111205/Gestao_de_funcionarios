from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from . import contrato_bp
from .modelos import Contratos
from app.funcionarios.modelos import Funcionarios
from app.banco_de_dados import db
from datetime import datetime
from app.auth.permissoes import permissao_requerida


@contrato_bp.route("/")
@login_required
def listar_contratos():
    contratos=Contratos.query.order_by(Contratos.data_inicio.desc()).all()
    return render_template("contratos/listar.html", contratos=contratos)

@contrato_bp.route("/cadastrar")
@login_required
def cadastrar_contratos():
    funcionario=Funcionarios.query.order_by(Funcionarios.nome_funcionario).all()
    return render_template("contratos/cadastrar.html",funcionario=funcionario)

@contrato_bp.route("/inserir", methods=["POST"])
@login_required
def criar_contrato():
    funcionario_id=request.form.get("funcionario_id")
    funcionario=Funcionarios.query.get_or_404(funcionario_id)
    contrato_ativo=Contratos.query.filter_by(
        funcionario_id=funcionario.id,
        ativo=True
    ).first()
    if contrato_ativo:
        flash("Este funcionario ja possui um contrato ativo.", "erro")
        return redirect(url_for("contrato.listar_contratos"))
    
    tipo=request.form.get("tipo").title()
    data_inicio=datetime.strptime(request.form.get("data_inicio"), "%Y-%m-%d").date()
    contrato=Contratos(
        funcionario_id=funcionario.id,
        tipo=tipo,
        data_inicio=data_inicio
    )
    db.session.add(contrato)
    db.session.commit()
    flash("Contrato criado com sucesso", "sucesso")
    return redirect(url_for("contrato.listar_contratos"))


@contrato_bp.route("/<int:funcionario_id>/encerrar")
@login_required
def encerrar_contrato(funcionario_id):
    contrato=Contratos.query.get_or_404(funcionario_id)
    funcionario=Funcionarios.query.get_or_404(funcionario_id)
    if not contrato.ativo:
        flash("Este contrato ja esta encerrado.", "erro")
        return redirect(url_for("contrato.listar_contratos"))
    contrato.encerrar()
    db.session.delete(funcionario)
    db.session.delete(contrato)
    db.session.commit()
    flash("Contrato encerrado com sucesso.", "sucesso")
    return redirect(url_for("contrato.listar_contratos"))
