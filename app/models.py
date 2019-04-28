import datetime
from extensions import db


class ReceitaIngrediente(db.Model):
    __tablename__ = "ReceitaIngrediente"

    id_receita = db.Column(db.Integer, db.ForeignKey('Receita.id'), primary_key=True)
    id_ingrediente = db.Column(db.Integer, db.ForeignKey('Ingrediente.id'), primary_key=True)
    porcentagem = db.Column(db.Float)
    filho = db.relationship("Ingrediente", back_populates="parentes")
    parente = db.relationship("Receita", back_populates="filhos")


class Ingrediente(db.Model):

    __tablename__ = "Ingrediente"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(60), nullable=False)
    parentes = db.relationship("ReceitaIngrediente", back_populates="filho")

    def __repr__(self):
        return '<Ingrediente {}>'.format(self.nome)

    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome
        }


class Receita(db.Model):

    __tablename__ = "Receita"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    adicionada_em = db.Column(db.DateTime, default=datetime.datetime.now)
    filhos = db.relationship("ReceitaIngrediente", back_populates="parente")

    def __repr__(self):
        return '<Receita {}>'.format(self.nome)

    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "descricao":self.descricao
        }
