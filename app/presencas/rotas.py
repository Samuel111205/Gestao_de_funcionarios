from flask import redirect, render_template, request, url_for
from flask_login import login_required
from .modelos import Presencas
from app.banco_de_dados import db
from app.funcionarios.modelos import Funcionarios
from . import presenca_bp
from datetime import datetime


@presenca_bp.route("/<int:funcionario_id>")
@login_required
def listar(funcionario_id):
    funcionario=Funcionarios.query.get_or_404(funcionario_id)
    return render_template("presencas/listar.html", funcionario=funcionario)


@presenca_bp.route("/registrar/<int:funcionario_id>", methods=["POST"])
@login_required
def registrar(funcionario_id):
    data=datetime.strptime(request.form.get("data"), "%Y-%m-%d").date()
    presente=request.form.get("presente") == "on"
    presenca=Presencas(
        funcionario_id=funcionario_id,
        data=data,
        presente=presente
    )
    db.session.add(presenca)
    db.session.commit()
    return redirect(url_for("presenca.listar", funcionario_id=funcionario_id))

