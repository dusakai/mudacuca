# -*- coding: utf-8 -*-
from flask import render_template

from app import app, db

from app.models.forms import LoginForm
from app.models.models import *

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

@app.route ('/privacy', methods=['GET', 'POST'])
def privacy ():
    privacy = User()
    return render_template('privacy.html',
    privacy=privacy)
