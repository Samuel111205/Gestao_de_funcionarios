from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user
from .modelos import Presencas
from app.banco_de_dados import db
from app.contratos.modelos import Contratos
from . import presenca_bp
from datetime import date, datetime


@presenca_bp.route("/contrato/<int:contrato_id>")
@login_required
def listar_presencas(contrato_id):
    contrato=Contratos.query.get_or_404(contrato_id)
    presencas=Presencas.query.filter_by(
        contrato_id=contrato.id
    ).order_by(Presencas.data.desc()).all()
    return render_template(
        "presencas/listar.html",
        contrato=contrato,
        presencas=presencas
    )

@presenca_bp.route("/registrar/entrada/<int:contrato_id>")
@login_required
def registrar_entrada(contrato_id):
    contrato=Contratos.query.get_or_404(contrato_id)
    hoje=date.today()
    presenca=Presencas.query.filter_by(
        contrato_id=contrato.id,
        data=hoje
    ).first()
    if presenca:
        flash("Presenca ja registrada hoje.", "erro")
        return redirect(url_for(
            "presenca.listar_presencas",
            contrato_id=contrato.id
        ))
    nova_presenca=Presencas(
        contrato_id=contrato.id
    )
    db.session.add(nova_presenca)
    db.session.commit()
    flash("Entrada registrada com sucesso.", "sucesso")
    return redirect(url_for(
        "presenca.listar_presencas",
        contrato_id=contrato.id
    ))


@presenca_bp.route("/registrar/saida/<int:presenca_id>")
@login_required
def registrar_saida(presenca_id):
    presenca=Presencas.query.get_or_404(presenca_id)
    if presenca.hora_saida:
        flash("Saida ja registrada.", "erro")
        return redirect(
            url_for(
                "presenca.listar_presencas",
                contrato_id=presenca.contrato_id
            )
        )
    presenca.registrar_saida()
    db.session.commit()
    flash("Saida registrada com sucesso.", "sucesso")
    return redirect(
        url_for(
            "presenca.listar_presencas",
            contrato_id=presenca.contrato_id
        )
    )
