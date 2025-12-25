from flask import render_template, request, redirect, url_for, session, flash
from . import auth_bp
from flask_login import logout_user, login_user, login_required, current_user
from app.usuarios.modelos import Usuarios

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method== "POST":
        email=request.form["email"]
        senha=request.form["senha"]
        usuario=Usuarios.query.filter_by(email=email).first()

        if usuario and usuario.check_senha(senha):
            login_user(usuario)
            flash("Login efectuado com sucesso", "sucess")
            return redirect(url_for("home.home"))

        flash("Email ou senha invalidos", "danger")
    return render_template("auth/login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    session.clear()
    flash("Sessão encerrada", "info")
    return redirect(url_for("auth.login"))
