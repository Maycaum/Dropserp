from crypt import methods
from flask import render_template, flash, redirect, url_for
from app import app
from app.models.form import LoginForm
from app.models.tables import User
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/menu')
def menu():
    return render_template('menu.html', name=current_user.username)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            print("logado")
            return redirect(url_for("rh"))
        else:
            flash('Login Invalido')
    return render_template('index.html', form=form)
    
@app.route('/estoque')
@login_required
def Estoque():
    return render_template("Estoque-menu.html")

@app.route('/estoque-cadastro')
@login_required
def EstoqueCadastro():
    return render_template("Estoque-cadastro-de-produto.html")

@app.route('/estoque-pesquisa')
@login_required
def EstoquePesquisa():
    return render_template("Estoque-pesquisar-produto.html")

@app.route('/financeiros-contas-a-pagar')
@login_required
def ContasAPagar():
    return render_template("financeiro-contas-a-pagar.html")

@app.route('/financeiro-contas-a-receber')
@login_required
def ContasAReceber():
    return render_template("financeiro-contas-a-receber.html")

@app.route('/financeiros-exibir-relatorio')
@login_required
def ExibirRelatorio():
    return render_template("financeiro-exibir-relatorio.html")

@app.route('/financeiro-menu')
@login_required
def Financeiro():
    return render_template("Financeiro-menu.html")

@app.route('/rh-menu')
@login_required
def rh():
    return render_template("RH-menu.html")

@app.route('/rh-funcionario')
@login_required
def RhFuncionarios():
    return render_template("RH-Funcionario.html")

@app.route('/rh-fornecedores')
@login_required
def Rh():
    return render_template("RH-Fornecedores.html") 