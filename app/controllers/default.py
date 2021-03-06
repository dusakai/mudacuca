# -*- coding: utf-8 -*-
from flask import render_template, request, flash, url_for, \
                    redirect, send_from_directory



from app import app, db

from app.models.forms import LoginForm, ProductForm, CustomerForm
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
        image_name = product_form.image_name.data
        description = product_form.description.data
        quantity = product_form.quantity.data
        purchase_price = product_form.purchase_price.data
        sale_price = product_form.sale_price.data
        minimum_in_stock = product_form.minimum_in_stock.data
        category = product_form.category.data
        stock = product_form.stock.data
        url_image = BASE_DIR+IMAGE_DIR+image_name

        #Product data add
        product_data = Product(name, description, quantity, purchase_price, sale_price, \
                            minimum_in_stock, url_image, category, stock)
        db.session.add(product_data)
        db.session.commit()
        db.session.close()


    product_form = ProductForm(request.form)
    if request.method == 'POST' and product_form.validate():
        if request.form.get("name") != None:
            populateProductTable()
            return redirect(url_for('product'))
    else:
        print (product_form.validate())

    product_items = db.session.query(Product.name, Product.category, \
                    Product.description, Product.quantity, \
                    Product.purchase_price, Product.sale_price, \
                    Product.stock, Product.minimum_in_stock).\
                    all()

    return render_template('product.html', product_form=product_form, \
                    product_items=product_items)


@app.route ('/customer', methods=['GET', 'POST'])
def customer ():

    def populateCustomerTable():
        name = customer_form.name.data
        email = customer_form.email.data
        image_name = customer_form.image_name.data
        cpf = customer_form.cpf.data
        category = customer_form.category.data
        phone = customer_form.phone.data
        address = customer_form.address.data

        url_image = BASE_DIR+IMAGE_DIR+image_name

        #Product data add
        customer_data = Customer(name, email, cpf, category, phone, address)
        db.session.add(customer_data)
        db.session.commit()
        db.session.close()


    customer_form = CustomerForm(request.form)

    if request.method == 'POST' and customer_form.validate():
        if request.form.get("name") != None:
            populateCustomerTable()
            return redirect(url_for('customer'))
    else:
        print (customer_form.validate())

    customer_person = db.session.query(Customer.name, Customer.email,\
                            Customer.cpf, Customer.category, \
                            Customer.phone, Customer.address).\
                            all()

    return render_template('customer.html', customer_form=customer_form, \
                    customer_person=customer_person)

@app.route ('/vendas', methods=['GET', 'POST'])
def vendas ():
    # vendas = User()
    vendas = 'vendas'
    if request.method == 'POST':
        # if request.files.get("file_dataset") != None:
        #     f_ds = request.files['file_dataset']
        pass

    return render_template('vendas.html', vendas=vendas)
