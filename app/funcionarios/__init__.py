from flask import Blueprint

funcionario_bp=Blueprint("funcionario", __name__, template_folder="../../templates/funcionarios")
from . import rotas