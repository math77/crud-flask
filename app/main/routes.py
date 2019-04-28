from flask import Blueprint, url_for, redirect, render_template, jsonify, request
from extensions import db
from app.models import Ingrediente, Receita, ReceitaIngrediente
from app.main.forms import NovoIngredienteForm, NovaReceitaForm


bp_main= Blueprint('main', __name__, url_prefix='/main')


@bp_main.route("/", methods=['GET', 'POST'])
def main():
    receitas = Receita.query.all()
    return render_template("main.html", receitas=receitas)


@bp_main.route("/novo_ingrediente", methods=['GET', 'POST'])
def novo_ingrediente():
    form = NovoIngredienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
        ingrediente = Ingrediente(nome=nome)
        db.session.add(ingrediente)
        db.session.commit()
        return redirect(url_for('main.novo_ingrediente'))
    return render_template("novo_ingrediente.html", form=form)


@bp_main.route("nova_receita", methods=['GET', 'POST'])
def nova_receita():
    form = NovaReceitaForm()
    if form.validate_on_submit():
        nome = form.nome.data
        descricao = form.descricao.data
        receita = Receita(nome=nome, descricao=descricao)

        db.session.add(receita)
        db.session.commit()
        db.session.refresh(receita)
        id_receita = receita.id

        ingred_query = Ingrediente.query.all()
        ingred_list = [i.to_dict() for i in ingred_query]
        return jsonify({'id_receita':id_receita, 'ingredientes':ingred_list})
    return render_template("nova_receita.html", form=form)

@bp_main.route("todas_receitas", methods=['GET'])
def todas_receitas():
    receitas = Receita.query.all()
    receitas_list = [receita.to_dict() for receita in receitas]
    return jsonify({'receitas': receitas_list})

@bp_main.route("ingrediente_receita", methods=['GET', 'POST'])
def ingrediente_receita():
    data = request.get_json()
    receita = Receita.query.filter_by(id=data['id_receita']).first()
    rec_ing = ReceitaIngrediente(porcentagem=data['porcentagem'])
    rec_ing.filho = Ingrediente.query.filter_by(id=data['id_ingrediente']).first()

    receita.filhos.append(rec_ing)

    db.session.add(receita)
    db.session.commit()
    return jsonify({'data':'Salvo com sucesso'})



@bp_main.route("calculo_quantidades", methods=['GET', 'POST'])
def calculo_quantidades():
    #pegar o id_receita e a quantidade que vem na requisição
    #faz uma query para pegar os ingredientes
    #faz o calculo da porcentagem de cada um e guarda em uma lista
    #retorna a lista para o front
    pass

def configure(app):
    app.register_blueprint(bp_main)
