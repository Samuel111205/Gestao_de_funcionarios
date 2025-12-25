from flask import Blueprint
presenca_bp=Blueprint("presenca", __name__, template_folder="../../templates/presencas")
from . import rotas

