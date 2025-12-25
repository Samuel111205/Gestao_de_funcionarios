from flask import Blueprint
contrato_bp=Blueprint("contrato", __name__, template_folder="../../templates/contratos")
from . import rotas
