
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class CadastroProdutos(FlaskForm):
    sku = StringField('sku', validators=[DataRequired()])
    nome = StringField('nome', validators=[DataRequired()])
    quantidade = IntegerField('quantidade', validators=[DataRequired()])
    preco = DecimalField('preço', validators=[DataRequired()])
    descricao = TextAreaField('Desccrição')

class CadastroLojista(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    nome = StringField('nome', validators=[DataRequired()])
    sobrenome = StringField('sobrenomenome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    senha = PasswordField('password', validators=[DataRequired()])

class CadastroFuncionario(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    sobrenome = StringField('sobrenomenome', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    cargo = SelectField('Cargo', validators=[DataRequired()], choices=[("Analista Rh"), ("Analista Estoque"), ("Analista Financeiro")])

class CadastroFornecedor(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])

class CadastroReceber(FlaskForm):
    identificador = StringField('identificador', validators=[DataRequired()])
    valor = IntegerField('valor', validators=[DataRequired()])
    pagador = StringField('pagador', validators=[DataRequired()])
    dia = DateField(validators=None, format='%Y-%m-%d')

class CadastroPagar(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    valor = IntegerField('valor', validators=[DataRequired()])
    pagador = StringField('pagador', validators=[DataRequired()])
    dia = DateField(validators=None, format='%Y-%m-%d')
