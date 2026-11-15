import os

import pymysql
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


def conectar():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor,
    )


@app.route("/")
def home():
    css_ = url_for('static', filename='css/style.css')
    return render_template('index.html', title="Home",
                           css_path=css_)


@app.route("/sobre")
def sobre():
    css_ = url_for('static', filename='css/style.css')
    return render_template('sobre.html', title="Sobre",
                           css_path=css_)


@app.route("/contato")
def contato():
    css_ = url_for('static', filename='css/style.css')
    return render_template('contato.html', title="Contato",
                           css_path=css_)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    css_ = url_for('static', filename='css/style.css')
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")

        if not nome or not email or not senha:
            flash("Preencha nome, e-mail e senha.")
            return render_template('cadastro.html', title="Cadastro",
                                   css_path=css_)
        senha_hash = generate_password_hash(senha)

        conn = conectar()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO usuarios (nome, email, senha) "
                    "VALUES (%s, %s, %s)",
                    (nome, email, senha_hash),
                )
            conn.commit()
        except pymysql.err.IntegrityError:
            flash("Este e-mail já está cadastrado.")
            return render_template('cadastro.html', title="Cadastro",
                                   css_path=css_)
        finally:
            conn.close()

        flash("Cadastro realizado com sucesso!")
        return redirect(url_for("listar"))

    return render_template('cadastro.html', title="Cadastro",
                           css_path=css_)


@app.route("/listar")
def listar():
    css_ = url_for('static', filename='css/style.css')
    conn = conectar()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nome, email FROM usuarios ORDER BY id")
            registros = cur.fetchall()
    finally:
        conn.close()
    return render_template('listar.html', title="Listagem",
                           css_path=css_, registros=registros)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
