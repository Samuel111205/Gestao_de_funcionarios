from flask import Blueprint
salario_bp=Blueprint("salario", __name__, template_folder="../../templates/salarios")
from . import rotas
