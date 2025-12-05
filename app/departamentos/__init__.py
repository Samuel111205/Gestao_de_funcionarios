from flask import Blueprint

departamento_bp=Blueprint("departamento",__name__, template_folder="../../templates/departamentos")
from . import rotas
