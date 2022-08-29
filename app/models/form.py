from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, TextAreaField
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