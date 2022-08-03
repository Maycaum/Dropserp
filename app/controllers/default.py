from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/estoque')
def Estoque():
    return render_template("Estoque-menu.html")

@app.route('/estoque-cadastro')
def EstoqueCadastro():
    return render_template("Estoque-cadastro-de-produto.html")

@app.route('/estoque-pesquisa')
def EstoquePesquisa():
    return render_template("Estoque-pesquisar-produto.html")
@app.route('/financeiros-contas-a-pagar')
def ContasAPagar():
    return render_template("financeiro-contas-a-pagar.html")

@app.route('/financeiro-contas-a-receber')
def ContasAReceber():
    return render_template("financeiro-contas-a-receber.html")

@app.route('/financeiros-exibir-relatorio')
def ExibirRelatorio():
    return render_template("financeiro-exibir-relatorio.html")

@app.route('/financeiro-menu')
def Financeiro():
    return render_template("Financeiro-menu.html")

@app.route('/rh-menu')
def rh():
    return render_template("RH-menu.html")

@app.route('/rh-funcionario')
def RhFuncionarios():
    return render_template("RH-Funcionario.html")

@app.route('/rh-fornecedores')
def Rh():
    return render_template("RH-Fornecedores.html") 