import datetime
from extensions import db


receita_ingrediente_assoc = db.Table('Receita_Ingrediente',
                                      db.Column('id_receita', db.Integer, db.ForeignKey('Receita.id'), primary_key=True),
                                      db.Column('id_ingrediente', db.Integer, db.ForeignKey('Ingrediente.id'), primary_key=True),
                                      db.Column('porcentagem', db.Float))



class Ingrediente(db.Model):

    __tablename__ = "Ingrediente"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(60), nullable=False)

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
    ingredientes = db.relationship("Ingrediente", secondary=receita_ingrediente_assoc)

    def __repr__(self):
        return '<Receita {}>'.format(self.nome)

    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "descricao":self.descricao
        }
