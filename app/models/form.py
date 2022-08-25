from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DecimalRangeField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class CadastroProdutos():
    sku = StringField('sku', validators=[DataRequired()])
    name = StringField('nome', validators=[DataRequired()])
    quantidade = IntegerField('quantidade', validators=[DataRequired()])
