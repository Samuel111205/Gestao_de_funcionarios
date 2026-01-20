from flask import render_template, request, redirect, url_for, session, flash
from . import usuario_bp
from flask_login import logout_user, login_user, login_required, current_user
from app.banco_de_dados import db
from app.auth.permissoes import permissao_requerida
from app.usuarios.modelos import Usuarios

@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    """if current_user.is_authenticated:
        return redirect(url_for("usuarios.dashboard"))
    """
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")

        # Validação básica dos campos
        if not email or not senha:
            flash("Email e senha são obrigatórios.", "warning")
            return render_template("usuarios/login.html")

        usuario = Usuarios.query.filter_by(email=email, ativo=True).first()

        if usuario and usuario.check_senha(senha):
            login_user(usuario)
            flash("Login efetuado com sucesso", "success")
            # Redireciona para o destino original se existir, senão para home
            next_page = request.args.get("next") or url_for("home.home")
            return redirect(next_page)

        flash("Email ou senha inválidos", "danger")
    return render_template("usuarios/login.html")


@usuario_bp.route("/logout")
@login_required
def logout():
    # Termina sessão do Flask-Login e limpa sessão
    logout_user()
    session.clear()
    flash("Sessão encerrada", "info")
    return redirect(url_for("usuarios.login"))

@usuario_bp.route("/criar_usuario", methods=["GET", "POST"])
@login_required
@permissao_requerida("administrador")
def criar_usuario():
    if request.method=="POST":
        nome=request.form.get("nome")
        email=request.form.get("email")
        senha=request.form.get("senha")

        if not nome or not email or not senha:
            flash("Todos os campos são obrigatorios.", "erro")
            return redirect(url_for("usuarios.criar_usuario"))

        if Usuarios.query.filter_by(email=email).first():
            flash("Email ja existe", "erro")
            return redirect(url_for("usuario.criar_usuario"))

        usuario=Usuarios(nome=nome, email=email)
        usuario.set_senha(senha)
        db.session.add(usuario)
        db.session.commit()
        flash("Usuarios cadastrado com sucesso,", "sucesso")
        return redirect(url_for("usuarios.login"))
    return render_template("criar_usuario.html")
