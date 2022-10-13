from datetime import date, datetime
from flask import render_template, flash, redirect, url_for, flash, jsonify
from app import app, db
from config import conn
from app.models.form import LoginForm, CadastroProdutos, CadastroLojista, CadastroFuncionario, CadastroFornecedor, CadastroReceber, CadastroPagar
from app.models.tables import Fornecedor, Funcionario, Pagar, Receber, User
from app.models.api import wcapi
from flask_login import login_user, logout_user, login_required, current_user
import sqlalchemy

@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("Dashboard"))
        else:
            flash('Login Invalido')
    return render_template('index.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('deslogado')
    return redirect(url_for('index'))


#dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def Dashboard():
    return render_template("dashboard.html", name=current_user.username)


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
        flash('Produto Criado com sucesso')
    return render_template("Estoque-cadastro-de-produto.html", name=current_user.username, cadastro=cadastro)


@app.route('/estoque-listar')
@login_required
def EstoqueListar():
    retorno = wcapi.get("products", params={"per_page": 20}).json()
    return render_template("Estoque-listar-produtos.html", name=current_user.username, retorno=retorno)

#Financeiro

@app.route('/financeiros-contas-a-pagar', methods=['GET', 'POST'])
@login_required
def ContasAPagar():
    pagar = CadastroPagar()
    if pagar.validate_on_submit():
        cadastro = Pagar(finalidade = pagar.finalidade.data,
                            valor= pagar.valor.data,
                            comprador=pagar.comprador.data,
                            clientefinal = pagar.clienteFinal.data,
                            data=pagar.dia.data)
        db.session.add(cadastro)
        db.session.commit()
        Receber.query.all()
        flash('Conta á pagar cadastrada com sucesso')
    return render_template("financeiro-contas-a-pagar.html", name=current_user.username, pagar=pagar)


@app.route('/financeiro-contas-a-receber', methods=['GET', 'POST'])
@login_required
def ContasAReceber():
    receber = CadastroReceber()
    if receber.validate_on_submit():
        cadastro = Receber(identificador = receber.identificador.data,
                            valor= receber.valor.data,
                            pagador=receber.pagador.data,
                            data=receber.dia.data)
        db.session.add(cadastro)
        db.session.commit()
        Receber.query.all()
        flash('Conta á receber cadastrada com sucesso')
    return render_template("financeiro-contas-a-receber.html", name=current_user.username, receber=receber)


@app.route('/financeiros-exibir-relatorio')
@login_required
def ExibirRelatorio():
    mes = datetime.now().month
    ano = datetime.now().year
    retorno = wcapi.get("orders", params={"after": f'{ano}-{mes}-01T00:00:00', "before":f'{ano}-{mes}-30T23:59:59', 'per_page': 100, 'status':'completed'}).json()
    pagar = f"select * from pagar where data BETWEEN '{ano}-{mes}-01 00:00:00' and '{ano}-{mes}-30 00:00:00'"
    pagar = db.session.execute(pagar)
    receber = f"select * from receber "
    receber = db.session.execute(receber)
    return render_template("financeiro-exibir-relatorio.html", name=current_user.username, pagar=pagar, receber=receber)


@app.route('/financeiro-menu')
@login_required
def Financeiro():
    return render_template("Financeiro-menu.html", name=current_user.username)

#RH

@app.route('/rh-menu')
@login_required
def rh():
    return render_template("RH-menu.html", name=current_user.username)


@app.route('/rh-funcionario', methods=['GET', 'POST'])
@login_required
def RhFuncionario():
    funcionario = CadastroFuncionario()
    if funcionario.validate_on_submit():
        cadastro = Funcionario(nome = funcionario.nome.data, 
                                sobrenome = funcionario.sobrenome.data, 
                                cpf = funcionario.cpf.data, 
                                cargo = funcionario.cargo.data)
        db.session.add(cadastro)
        db.session.commit()
        Funcionario.query.all()
        flash('funcionario cadastrado com sucesso')
    return render_template("RH-Funcionario.html", name=current_user.username, funcionario = funcionario)


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
        flash('Lojista criado com sucesso')
    return render_template("RH-lojista.html", name=current_user.username, cadastro=cadastro)
    # return jsonify(lojista)


@app.route('/rh-fornecedores', methods=['GET', 'POST'])
@login_required
def Rh():
    fornecedor = CadastroFornecedor()
    if fornecedor.validate_on_submit():
        cadastro = Fornecedor(nome=fornecedor.nome.data,
                              cnpj=fornecedor.cnpj.data,
                              descricao=fornecedor.descricao.data)
        db.session.add(cadastro)
        db.session.commit()
        Fornecedor.query.all()
        flash('Fornecedor criado com sucesso')
    return render_template("RH-Fornecedores.html", name=current_user.username, fornecedor=fornecedor)


