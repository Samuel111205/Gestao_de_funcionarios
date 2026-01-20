from flask import Blueprint

usuario_bp=Blueprint("usuarios",__name__, template_folder="../../templates/usuarios")
from . import rotas
