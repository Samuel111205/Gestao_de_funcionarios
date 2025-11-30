from banco_de_daos import db, app

class Departamentos(db.Model):
    departamento_id=db.Column(db.Integer, primary_key=True)
    nome_departamento=db.Column(db.String(120), nullable=False)


class Cargos(db.Model):
    cargo_id=db.Column(db.Integer, primary_key=True)
    nome_cargo=db.Column(db.String(120), nullable=False)


class Funcionarios(db.Model):
    funcionario_id=db.Column(db.Integer, primary_key=True)
    nome_funcionario=db.Column(db.String(120), nullable=False)
    data_nascimento=db.Column(db.Date, nullable=False)
    genero=db.Column(db.String(20), nullable=False)
    estado_civil=db.Column(db.String(40), nullable=False)
    email=db.Column(db.Text, unique=True, nullable=False)
    departamento_id=db.Column(db.Integer, db.ForeignKey('departamentos.departamento_id'), nullable=False)
    cargo_id=db.Column(db.Integer, db.ForeignKey('cargos.cargo_id'), nullable=False)


class Presencas(db.Model):
    presenca_id=db.Column(db.Integer, primary_key=True)
    funcionario_id=db.Column(db.Integer, db.ForeignKey('funcionarios.funcionario_id'), nullable=False)
    data=db.Column(db.Date, nullable=False)
    presente=db.Column(db.Boolean, nullable=False)

class Contratos(db.Model):
    licenca_id=db.Column(db.Integer, primary_key=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.funcionario_id'), nullable=False)
    tipo_licenca=db.Column(db.Text, nullable=False)
    data_inicio=db.Column(db.Date, nullable=False)
    data_fim=db.Column(db.Date, nullable=False)
    estado=db.Column(db.Text, nullable=False)

class Salarios(db.Model):
    salario_id=db.Column(db.Integer, primary_key=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.funcionario_id'), nullable=False)
    salario_diario=db.Column(db.Float)
    salario_mensal=db.Column(db.Float)
    salario_descontado=db.Column(db.Float)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
