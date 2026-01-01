from app.banco_de_dados import db
from calendar import monthrange
from app.presencas.modelos import Presencas
from app.salarios.modelos import Salarios
from app.contratos.modelos import Contratos


def calcular_salario_mensal( mes, ano):
    #Contrato ativo
    contratos=Contratos.query.filter_by(ativo=True).all()
    for contrato in contratos:
        funcionario=contrato.funcionario
        salario_base=contrato.salario_base
        total_dias_mes=monthrange(ano, mes)[1]
        presencas=Presencas.query.filter(
            Presencas.funcionario_id==funcionario.id,
            Presencas.data.month==mes,
            Presencas.data.year==ano
        ).all()
        dias_trabalhadas=sum(1 for p in presencas if p.presente)
        faltas=total_dias_mes-dias_trabalhadas
        valor_dia=salario_base/total_dias_mes
        desconto_faltas=faltas*valor_dia
        valor_final=salario_base-desconto_faltas
        salario=Salarios(
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
