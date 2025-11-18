from flask import *
from database.banco_de_daos import conectar
from database.criar_tabelas import criar_tabela

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template("/cadastro.html")

@app.route('/cadastrados', methods=['POST'])
def cadastrados():
    conn=conectar()
    cursor=conn.cursor()

    criar_tabela()
    nome=request.form["nome"]
    data_nascimento=request.form["data_nascimento"]
    genero=request.form["genero"]
    estado_civil=request.form["estado_civil"]
    email=request.form["email"]
    telefone=request.form["telefone"]

    cursor.execute("""
        INSERT INTO funcionario(
            nome,
            data_nascimento,
            genero,
            estado_civil,
            email,
            telefone 
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,(nome,data_nascimento,genero,estado_civil,email,telefone ))
    conn.commit()
    conn.close()

    return redirect('/cadastro')

@app.route('/lista')
def lista():
    conn=conectar()
    cursor=conn.cursor()

    criar_tabela()
    cursor.execute("SELECT id, nome, email, telefone FROM funcionario ORDER BY nome")
    dados=cursor.fetchall()
    conn.close()
    return render_template("lista.html",funcionarios=dados)


if __name__=="__main__":
    app.run(debug=True)