from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)