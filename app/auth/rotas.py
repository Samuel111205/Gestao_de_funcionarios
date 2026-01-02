from flask import render_template, request, redirect, url_for, session, flash
from . import auth_bp
from flask_login import logout_user, login_user, login_required
from app.usuarios.modelos import Usuarios

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")

        # Validação básica dos campos
        if not email or not senha:
            flash("Email e senha são obrigatórios.", "warning")
            return render_template("auth/login.html")

        usuario = Usuarios.query.filter_by(email=email).first()

        if usuario and usuario.check_senha(senha):
            login_user(usuario)
            flash("Login efetuado com sucesso", "success")
            # Redireciona para o destino original se existir, senão para home
            next_page = request.args.get("next") or url_for("home.home")
            return redirect(next_page)

        flash("Email ou senha inválidos", "danger")
    return render_template("auth/login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    # Termina sessão do Flask-Login e limpa sessão
    logout_user()
    session.clear()
    flash("Sessão encerrada", "info")
    return redirect(url_for("auth.login"))
