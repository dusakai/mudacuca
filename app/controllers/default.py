# -*- coding: utf-8 -*-
from flask import render_template, request, flash, url_for, \
                    redirect, send_from_directory



from app import app, db

from app.models.forms import LoginForm, ProductAdd
from app.models.models import *

# from app.controllers.functions import *


# variaveis
BASE_DIR = 'app/static/'
IMAGE_DIR = 'product_image/'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/index/<user>')
@app.route ('/', defaults={'user':None})
def index(user):
    return render_template('index.html',
    user=user)

@app.route ('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html',
    form=form)

@app.route ('/product', methods=['GET', 'POST'])
def product ():

    def populateProductTable():
        name = product_form.name.data
        image_name = product_form.url_image.data
        description = product_form.description.data
        quantity = product_form.quantity.data
        purchase_price = product_form.purchase_price.data
        sale_price = product_form.sale_price.data
        minimum_in_stock = product_form.minimum_in_stock.data
        category = product_form.category.data
        stock = product_form.stock.data

        # submit = request.form.get('submit')

        print ('product name: \n {}'.format(name))
        print ('product description: \n {}'.format(description))
        print ('product quantity: \n {}'.format(quantity))
        print ('product purchase_price: \n {}'.format(purchase_price))
        print ('product sale_price: \n {}'.format(sale_price))
        print ('product minimum_in_stock: \n {}'.format(minimum_in_stock))
        print ('product url_image: \n {}'.format(image_name))
        print ('product category: \n {}'.format(category))
        print ('product stock: \n {}'.format(stock))
        # print ('product submit: \n {}'.format(request.form.get('submit')))
        # check if the post request has the file part

    product_form = ProductAdd(request.form)
    if request.method == 'POST' and product_form.validate():
        if request.form.get("name") != None:
            populateProductTable()
    else:
        print (product_form.validate())

    return render_template('product.html', product_form=product_form)


@app.route ('/vendas', methods=['GET', 'POST'])
def vendas ():
    # vendas = User()
    vendas = 'vendas'
    if request.method == 'POST':
        # if request.files.get("file_dataset") != None:
        #     f_ds = request.files['file_dataset']
        pass

    return render_template('vendas.html', vendas=vendas)
