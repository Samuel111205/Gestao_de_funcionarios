from app.banco_de_dados import db
from calendar import monthrange
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from app.presencas.modelos import Presencas
from app.salarios.modelos import Salarios
from app.contratos.modelos import Contratos


def calcular_salario_mensal(mes, ano):
    """
    Calcula salários mensais para contratos ativos no mês/ano fornecidos.
    - Usa extract() para filtrar mês/ano no banco.
    - Conta dias úteis do mês para cálculo de desconto por falta.
    - Conta dias trabalhados únicos (por data) onde presente == True.
    - Atualiza registro existente de Salarios ou cria novo.
    """
    contratos = Contratos.query.filter_by(ativo=True).all()
    if not (1 <= mes <= 12):
        raise ValueError("Parâmetro 'mes' inválido")
    # itera contratos dentro de transação
    try:
        for contrato in contratos:
            funcionario = contrato.funcionario
            salario_base = contrato.salario_base

            # dias no mês e dias úteis (segunda a sexta)
            _, days_in_month = monthrange(ano, mes)
            total_dias_uteis = sum(
                1 for d in range(1, days_in_month + 1)
                if date(ano, mes, d).weekday() < 5
            )

            # buscar presenças do funcionário no mês usando extract()
            presencas = Presencas.query.filter(
                Presencas.funcionario_id == funcionario.id,
                SQLAlchemy.extract('month', Presencas.data) == mes,
                SQLAlchemy.extract('year', Presencas.data) == ano
            ).all()

            # contar dias únicos com presença marcada (evita múltiplos registros por dia)
            datas_presentes = set()
            for p in presencas:
                if getattr(p, "presente", False):
                    d = p.data
                    # se data for datetime, converte para date
                    try:
                        d_only = d.date()
                    except Exception:
                        d_only = d
                    datas_presentes.add(d_only)
            dias_trabalhadas = len(datas_presentes)

            # garante não negativo
            faltas = max(0, total_dias_uteis - dias_trabalhadas)

            # evita divisão por zero
            if total_dias_uteis > 0:
                valor_dia = salario_base / total_dias_uteis
            else:
                valor_dia = 0

            desconto_faltas = faltas * valor_dia
            valor_final = salario_base - desconto_faltas

            # evita duplicar registros de Salarios
            existente = Salarios.query.filter_by(
                contrato_id=contrato.id, mes=mes, ano=ano
            ).first()

            if existente:
                existente.salario_base = salario_base
                existente.dias_trabalhadas = dias_trabalhadas
                existente.faltas = faltas
                existente.descontos = desconto_faltas
                existente.acrescimos = 0
                existente.valor_final = valor_final
                db.session.add(existente)
            else:
                salario = Salarios(
                    contrato_id=contrato.id,
                    mes=mes,
                    ano=ano,
                    salario_base=salario_base,
                    dias_trabalhadas=dias_trabalhadas,
                    faltas=faltas,
                    descontos=desconto_faltas,
                    acrescimos=0,
                    valor_final=valor_final
                )
                db.session.add(salario)

        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
