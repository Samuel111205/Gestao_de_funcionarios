from flask import request, render_template, redirect, url_for
from flask_login import login_required
from . import salario_bp
from .modelos import Salarios
from app.funcionarios.modelos import Funcionarios
from app.banco_de_dados import db
from datetime import datetime

@salario_bp.route("/<int:funcionario_id>")
@login_required
def listar(funcionario_id):
    funcionario=Funcionarios.query.get_or_404(funcionario_id)
    return render_template("salarios/listar.html", funcionario=funcionario)


@salario_bp.route("/inserir/<int:funcionario_id>", methods=["POST"])
@login_required
def inserir(funcionario_id):
    valor=request.form.get("valor")
    data_inicio=datetime.strptime(request.form.get("data_inicio"), "%Y-%m-%d").date()
    salario=Salarios(valor=valor, data_inicio=data_inicio, funcionario_id=funcionario_id)
    db.session.add(salario)
    db.session.commit()
    return redirect(url_for("salario.listar", funcionario_id=funcionario_id))

