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

#Financeiro
class Financeiro(db.Model):
    __tablename__ = "financeiro"

    movimento = db.Column(db.Integer, primary_key=True) # Id da transação
    receber = db.Column(db.Integer)
    pagar = db.Column(db.Integer)
    sku_Estoque = db.Column(db.Integer, db.ForeignKey('estoque.sku'))
    #id_Fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedor.sku'))

    sku = db.relationship('Estoque', foreign_keys=sku_Estoque)
    #id = db.relationship('Fornecedor', foreign_keys=id_Fornecedor)

    def __init__(self, movimento, receber, pagar, sku_Estoque, id_Fornecedor):
        self.movimento = movimento
        self.receber = receber
        self.pagar = pagar
        self.sku_Estoque = sku_Estoque
       #self.id_Fornecedor = id_Fornecedor

       