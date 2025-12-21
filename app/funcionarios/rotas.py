from flask import render_template, request, redirect, url_for
from . import funcionario_bp
from .modelos import Funcionarios
from app.banco_de_dados import db
from app.cargos.modelos import Cargos
from datetime import datetime

#Listar todos os funcionarios em ordem alfabetica
@funcionario_bp.route("/")
def listar_funcionarios():
    page=request.args.get('page',1, type=int)#Cria pagina no html
    funcionarios=Funcionarios.query.order_by(Funcionarios.nome_funcionario).paginate(page=page, per_page=10)
    return render_template("funcionarios/listar_funcionarios.html", funcionarios=funcionarios)

@funcionario_bp.route("/cadastrar")
def cadastrar_funcionario():
    cargos=Cargos.query.order_by(Cargos.nome_cargo).all()
    return render_template("funcionarios/cadastrar_funcionarios.html", cargos=cargos)

@funcionario_bp.route("/inserir", methods=["POST"])
def inserir_funcionario():
    nome = request.form.get("nome", "").strip().title()
    data_nascimento =datetime.strptime(request.form.get("data_nascimento"), "%Y-%m-%d").date()
    genero = request.form.get("genero").strip()
    estado_civil = request.form.get("estado_civil").strip()
    email = request.form.get("email").strip().lower()
    telefone = request.form.get("telefone").strip()
    cargo_id = request.form.get("cargo_id")

    #Validações dos campos
    if not (nome and data_nascimento and genero and estado_civil and email and telefone and cargo_id):
        return "Preencha todos os campos", 400
    #Verificar cargo
    if not Cargos.query.get(cargo_id):
        return "Cargo não encotrado", 400
    #Verificar email duplicados
    #if Funcionarios.query.filter_by(email=email).filter_by():
        #return "Email ja existe adicione outro email", 400

    funcionario = Funcionarios(
        nome_funcionario=nome,
        data_nascimento=data_nascimento,
        genero=genero,
        estado_civil=estado_civil,
        email=email,
        telefone=telefone,
        cargo_id=cargo_id
    )
    db.session.add(funcionario)
    db.session.commit()
    return redirect(url_for("funcionario.listar_funcionarios"))

@funcionario_bp.route("/editar/<int:funcionario_id>")
def editar_funcionario(funcionario_id):
    funcionario=Funcionarios.query.get_or_404(funcionario_id)
    cargos=Cargos.query.order_by(Cargos.nome_cargo).all()
    return render_template("funcionario/editar_funcionarios.html", funcionario=funcionario, cargos=cargos)

@funcionario_bp.route("/atualizar/<int:funcionario_id>", methods=["POST"])
def atualizar_funcionario(funcionario_id):
    funcionario = Funcionarios.query.get_or_404(funcionario_id)
    funcionario.nome_fucionario=request.form.get('nome', funcionario.nome_fucionario).strip().title()
    funcionario.estado_civil=request.form.get('estado_civil', funcionario.estado_civil).strip()
    funcionario.email=request.form.get('email', funcionario.email).strip().lower()
    funcionario.telefone=request.form.get('telefone', funcionario.telefone).strip()
    cargo_id=request.form.get('cargo_id', funcionario.cargo_id)

    #Verificar cargo e email duplicado
    if not Cargos.query.get(cargo_id):
        return "Cargo não encotrado"
    existe=Funcionarios.query.filter(Funcionarios.email==funcionario.email,Funcionarios.id!=funcionario.id).first()
    if existe:
        return "Email ja esta sendo utilizado por outro funcionario", 400

    funcionario.cargo_id=cargo_id
    db.session.commit()

    return redirect(url_for("funcionario.listar_funcionarios"))

@funcionario_bp.route("/deletar/<int:funcionario_id>", methods=["POST"])
def deletar_funcionario(funcionario_id):
    fucionario=Funcionarios.query.get_or_404(funcionario_id)
    db.session.delete(fucionario)
    db.session.commit()
    return redirect(url_for("funcionario.listar_funcionarios"))
