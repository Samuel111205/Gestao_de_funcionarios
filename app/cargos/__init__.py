from flask import Blueprint

cargo_bp=Blueprint("cargos",__name__, template_folder="../../templates/cargos")
from . import rotas
