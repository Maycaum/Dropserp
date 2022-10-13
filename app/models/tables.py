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
    cpf = db.Column(db.String(14),unique=True)
    cargo =  db.Column(db.String(25))

    def __init__(self, nome, sobrenome, cpf, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.cargo = cargo

    def __repr__(self):
        return "<Funcionario %r>" % self.nome

class Fornecedor(db.Model):
    __tablename__ = "fornecedor"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome = db.Column(db.String(50))
    cnpj = db.Column(db.String(20),unique=True)
    descricao = db.Column(db.String(50))

    def __init__(self, nome, cnpj, descricao):
        self.nome = nome
        self.cnpj = cnpj      
        self.descricao = descricao

    def __repr__(self):
        return "<Fornecedor %r>" % self.nome

#Financeiro
class Pagar(db.Model):
    __tablename__ = "pagar"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    finalidade = db.Column(db.String(25))
    valor = db.Column(db.Float)
    clientefinal = db.Column(db.String(25))
    comprador = db.Column(db.String(25))
    data = db.Column(db.DateTime)

    def __init__(self, finalidade, valor, clientefinal, comprador, data):
        self.finalidade = finalidade
        self.valor = valor
        self.clientefinal = clientefinal
        self.comprador = comprador
        self.data = data

    def __repr__(self):
        return "<Pagar %r>" % self.nome

class Receber(db.Model):
    __tablename__ = "receber"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    identificador = db.Column(db.String(25))
    valor = db.Column(db.Float)
    pagador = db.Column(db.String(25))
    data = db.Column(db.DateTime)

    def __init__(self, identificador, valor, pagador, data):
        self.identificador = identificador
        self.valor = valor
        self.pagador = pagador
        self.data = data

    def __repr__(self):
        return "<Receber %r>" % self.identificador