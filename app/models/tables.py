from app import db
from app import lm

@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))



    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return "<User %r>" % self.username

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

#Estoque
class Estoque(db.Model):
    __tablename__ = "estoque"

    sku = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nome = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.String(50))
    descricao = db.Column(db.Text)

    def __init__(self, sku, nome, quantidade, preco, descricao):
        self.sku = sku
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao

    def __repr__(self):
        return "<Estoque %r>" % self.nome

#RH
class Funcionario(db.Model):
    __tablename__ = "funcionario"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(25))
    sobrenome = db.Column(db.String(25))
    cpf = db.Column(db.Integer,unique=True)
    cargo =  db.Column(db.String(25))
    senha = db.Column(db.String(50))

    def __init__(self, nome, sobrenome, cpf, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.cargo = cargo

    def __repr__(self):
        return "<Funcionario %r>" % self.nome

class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user = db.Column(db.String(25), unique=True)
    nome = db.Column(db.String(25))
    sobrenome = db.Column(db.String(25))
    email = db.Column(db.String(25),unique=True)
    senha = db.Column(db.String(50))

    def __init__(self, user, nome, sobrenome, email, senha):
        self.user = user
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha        

    def __repr__(self):
        return "<Cliente %r>" % self.nome

#Financeiro
class Pagar(db.Model):
    __tablename__ = "pagar"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(25))
    valor = db.Column(db.Integer)
    pagador = db.Column(db.String(25))
    data = db.Column(db.DateTime)

    def __init__(self, nome, valor, pagador, data):
        self.nome = nome
        self.valor = valor
        self.pagador = pagador
        self.data = data

    def __repr__(self):
        return "<Pagar %r>" % self.nome

class Receber(db.Model):
    __tablename__ = "receber"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(25))
    valor = db.Column(db.Integer)
    pagador = db.Column(db.String(25))
    data = db.Column(db.DateTime)

    def __init__(self, nome, valor, pagador, data):
        self.nome = nome
        self.valor = valor
        self.pagador = pagador
        self.data = data

    def __repr__(self):
        return "<Receber %r>" % self.nome