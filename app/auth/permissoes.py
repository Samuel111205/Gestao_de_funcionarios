from flask_login import current_user
from functools import wraps
from flask import abort

def permissao_requerida(nome, verificar_area=False):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.tem_permissao(nome):
                abort(403)
            if verificar_area and not current_user.is_admin():
                funcionario=kwargs.get("funcionario")
                if funcionario and funcionario.departamento_id != current_user.departamento_id:
                    abort(403)
            return func(*args, **kwargs)
        return wrapper
    return decorador

