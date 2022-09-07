from tkinter.messagebox import RETRY
from flask import render_template, flash, redirect, url_for, jsonify
from app import app
from app.models.form import LoginForm, CadastroProdutos, CadastroLojista
from app.models.tables import User
from app.models.api import wcapi
from flask_login import login_user, logout_user, login_required, current_user
import json

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

@app.route('/logout')
def logout():
    logout_user()
    flash('deslogado')
    return redirect(url_for('index'))
    
@app.route('/estoque')
@login_required
def Estoque():
    return render_template("Estoque-menu.html", name=current_user.username)

@app.route('/estoque-cadastro', methods=['GET', 'POST'])
@login_required
def EstoqueCadastro():
    cadastro = CadastroProdutos()
    if cadastro.validate_on_submit():
        produto = {
            "sku": cadastro.sku.data,
            "name": cadastro.nome.data,
            "regular_price": str(cadastro.preco.data),
            'manage_stock': True,
            "stock_quantity": cadastro.quantidade.data,
            "description": cadastro.descricao.data,
            }
        wcapi.post("products", produto).json()
        flash('Produto Criado')
    return render_template("Estoque-cadastro-de-produto.html", name=current_user.username, cadastro=cadastro)

@app.route('/estoque-pesquisa')
@login_required
def EstoqueListar():
    retorno = wcapi.get("products", params={"per_page": 20}).json()
    return render_template("Estoque-listar-produtos.html", name=current_user.username, retorno=retorno)

@app.route('/financeiros-contas-a-pagar')
@login_required
def ContasAPagar():
    return render_template("financeiro-contas-a-pagar.html", name=current_user.username)

@app.route('/financeiro-contas-a-receber')
@login_required
def ContasAReceber():
    return render_template("financeiro-contas-a-receber.html", name=current_user.username)

@app.route('/financeiros-exibir-relatorio')
@login_required
def ExibirRelatorio():
    return render_template("financeiro-exibir-relatorio.html", name=current_user.username)

@app.route('/financeiro-menu')
@login_required
def Financeiro():
    return render_template("Financeiro-menu.html", name=current_user.username)

@app.route('/rh-menu')
@login_required
def rh():
    return render_template("RH-menu.html", name=current_user.username)

@app.route('/rh-funcionario')
@login_required
def RhFuncionario():
    return render_template("RH-Funcionario.html", name=current_user.username)

@app.route('/rh-lojista', methods=['GET', 'POST'])
@login_required
def RhLojista():
    cadastro = CadastroLojista()
    if cadastro.validate_on_submit():
        lojista = {
            "email": cadastro.email.data,
            "first_name": cadastro.nome.data,
            "last_name": cadastro.sobrenome.data,
            "role": "teste",
            "username": cadastro.username.data,
            "password": cadastro.senha.data,
        }
        wcapi.post("customers", lojista).json()
        flash('lojista criado')
    return render_template("RH-lojista.html", name=current_user.username, cadastro=cadastro)
        #return jsonify(lojista)

@app.route('/rh-fornecedores')
@login_required
def Rh():
    return render_template("RH-Fornecedores.html", name=current_user.username) 

