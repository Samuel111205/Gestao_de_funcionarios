from flask_login import current_user
from functools import wraps
from flask import redirect, url_for, flash

def administrador_required(f):
    @wraps(f)
    def permissoes_funcao(*args, **kwargs):
        if not current_user.is_admin():
            flash("Acesso restrito ao administrador", "danger")
            return redirect(url_for("home.home"))
        return f(*args, **kwargs)
    return permissoes_funcao

