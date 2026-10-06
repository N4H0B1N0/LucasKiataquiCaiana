from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
 return "<h1>Página inicial</h1>"
@app.route("/sobre")
def sobre():
 return "<h1>Sobre nós</h1><p>Esta é a página sobre.</p>"
@app.route("/contato")
def contato():
 return "<h1>Contato</h1><p>email@exemplo.com</p>"