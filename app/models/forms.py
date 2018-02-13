from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, \
                    TextField, IntegerField, FloatField , SubmitField, \
                    FileField, validators, widgets
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class LoginForm (FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")


class ProductForm (FlaskForm):
    """
    Form for product add
    """

    name = StringField('Nome', validators=[DataRequired("Ops... :(\nInsira um nome para seu produto!")])
    description = TextField('Descrição', widget=TextArea())
    quantity = IntegerField ('Quantidade', validators=[DataRequired()])
    purchase_price = FloatField ('Preço de compra')
    sale_price = FloatField ('Preço de venda', validators=[DataRequired()])
    minimum_in_stock = IntegerField('Minimo em estoque')
    image_name = FileField('Imagem')
    category = StringField('Categoria')
    stock = StringField('Estoque', validators=[DataRequired()])
    submit = SubmitField('Inserir')

class CustomerForm (FlaskForm):
    """
    Form for customer add
    """

    name = StringField('Nome', validators=[DataRequired("Ops... :(\nInsira o nome do cliente!")])
    email = StringField('Email')
    cpf = StringField('CPF')
    phone = StringField('Fone')
    address = TextField('Endereço', widget=TextArea())
    image_name = FileField('Imagem')
    category = StringField('Categoria')
    submit = SubmitField('Inserir')
