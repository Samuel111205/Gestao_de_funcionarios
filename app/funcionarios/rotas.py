from flask import render_template, request, redirect, url_for
from . import funcionario_bp
from .modelos import Funcionarios
from app.banco_de_dados import db
from app.cargos.modelos import Cargos
from datetime import datetime
from flask_login import login_required


# Listar todos os funcionarios em ordem alfabetica
@funcionario_bp.route("/")
@login_required
def listar_funcionarios():
    page = request.args.get('page', 1, type=int)  # Cria pagina no html
    funcionarios = Funcionarios.query.order_by(Funcionarios.nome_funcionario).paginate(page=page, per_page=10)
    return render_template("funcionarios/listar_funcionarios.html", funcionarios=funcionarios)


@funcionario_bp.route("/cadastrar")
@login_required
def cadastrar_funcionario():
    cargos = Cargos.query.order_by(Cargos.nome_cargo).all()
    return render_template("funcionarios/cadastrar_funcionarios.html", cargos=cargos)


@funcionario_bp.route("/inserir", methods=["POST"])
@login_required
def inserir_funcionario():
    nome = request.form.get("nome", "").strip().title()
    data_str = request.form.get("data_nascimento", "").strip()
    genero = request.form.get("genero", "").strip()
    estado_civil = request.form.get("estado_civil", "").strip()
    email = request.form.get("email", "").strip().lower()
    telefone = request.form.get("telefone", "").strip()
    cargo_id_raw = request.form.get("cargo_id", "").strip()

    # Validações dos campos básicos
    if not (nome and data_str and genero and estado_civil and email and telefone and cargo_id_raw):
        return "Preencha todos os campos", 400

    # Parse da data com tratamento de erro
    try:
        data_nascimento = datetime.strptime(data_str, "%Y-%m-%d").date()
    except ValueError:
        return "Formato de data inválido. Use AAAA-MM-DD", 400

    # Converter cargo_id para int
    try:
        cargo_id = int(cargo_id_raw)
    except ValueError:
        return "ID do cargo inválido", 400

    # Verificar cargo
    if not Cargos.query.get(cargo_id):
        return "Cargo não encontrado", 400

    # Verificar email duplicado
    if Funcionarios.query.filter_by(email=email).first():
        return "Email já existe, adicione outro email", 400

    funcionario = Funcionarios(
        nome_funcionario=nome,
        data_nascimento=data_nascimento,
        genero=genero,
        estado_civil=estado_civil,
        email=email,
        telefone=telefone,
        cargo_id=cargo_id,
    )
    db.session.add(funcionario)
    db.session.commit()
    return redirect(url_for(f"{funcionario_bp.name}.listar_funcionarios"))


@funcionario_bp.route("/editar/<int:funcionario_id>")
@login_required
def editar_funcionario(funcionario_id):
    funcionario = Funcionarios.query.get_or_404(funcionario_id)
    cargos = Cargos.query.order_by(Cargos.nome_cargo).all()
    return render_template("funcionarios/editar_funcionarios.html", funcionario=funcionario, cargos=cargos)


@funcionario_bp.route("/atualizar/<int:funcionario_id>", methods=["POST"])
@login_required
def atualizar_funcionario(funcionario_id):
    funcionario = Funcionarios.query.get_or_404(funcionario_id)

    nome_raw = request.form.get('nome', "").strip()
    if nome_raw:
        funcionario.nome_funcionario = nome_raw.title()

    estado_civil_raw = request.form.get('estado_civil', "").strip()
    if estado_civil_raw:
        funcionario.estado_civil = estado_civil_raw

    email_raw = request.form.get('email', "").strip().lower()
    if email_raw:
        funcionario.email = email_raw

    telefone_raw = request.form.get('telefone', "").strip()
    if telefone_raw:
        funcionario.telefone = telefone_raw

    cargo_id_raw = request.form.get('cargo_id', None)
    if cargo_id_raw is None or cargo_id_raw == "":
        cargo_id = funcionario.cargo_id
    else:
        try:
            cargo_id = int(cargo_id_raw)
        except ValueError:
            return "ID do cargo inválido", 400

    # Verificar cargo e email duplicado
    if not Cargos.query.get(cargo_id):
        return "Cargo não encontrado", 400

    existe = Funcionarios.query.filter(Funcionarios.email == funcionario.email, Funcionarios.id != funcionario.id).first()
    if existe:
        return "Email já está sendo utilizado por outro funcionário", 400

    funcionario.cargo_id = cargo_id
    db.session.commit()

    return redirect(url_for(f"{funcionario_bp.name}.listar_funcionarios"))


@funcionario_bp.route("/deletar/<int:funcionario_id>", methods=["POST"])
@login_required
def deletar_funcionario(funcionario_id):
    funcionario = Funcionarios.query.get_or_404(funcionario_id)
    db.session.delete(funcionario)
    db.session.commit()
    return redirect(url_for(f"{funcionario_bp.name}.listar_funcionarios"))


@funcionario_bp.route("/verdados/<int:funcionario_id>", methods=["GET"])
@login_required
def ver_dados_do_funcionario(funcionario_id):
    funcionario = Funcionarios.query.get_or_404(funcionario_id)
    return render_template("funcionarios/funcionarios_detalhes.html", funcionario=funcionario)
