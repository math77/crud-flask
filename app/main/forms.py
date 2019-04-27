from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, HiddenField, DecimalField
from wtforms.validators import DataRequired


class NovoIngredienteForm(FlaskForm):

    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Salvar')


class NovaReceitaForm(FlaskForm):

    nome = StringField('Nome', validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    submit = SubmitField('Salvar')
