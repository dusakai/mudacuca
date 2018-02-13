# -*- coding: utf-8 -*-
import json
import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, \
    Enum, DateTime, Numeric, Text, Unicode, UnicodeText
from sqlalchemy import event
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref, sessionmaker
#from sqlalchemy_i18n import make_translatable, translation_base, Translatable
import sqlite3

#make_translatable (options={'locales': ['pt', 'en', 'es'],
#                           'auto_create_locales': True,
#                           'fallback_locale': 'en'})

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    people_id = Column(Integer,
                        ForeignKey("people.id"), nullable=False)
    people = relationship("People", foreign_keys=[people_id],
                               backref=backref(
                                   "user",
                                   cascade="all, delete-orphan"))

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


    def __repr__ (self):
        return

class Category (db.Model):
    """ Category's table """
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    category_node_id = db.Column(db.Integer)
    node = db.Column(Boolean, nullable=False, default=True)
    leaf = db.Column(Boolean, nullable=False, default=True)
    slug = db.Column(db.String())

    def __init__(self, name, color, category_node_id, node, leaf):
        self.name = name
        self.color = color
        self.category_node_id = category_node_id
        self.node = node
        self.leaf = leaf

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)

class Stock (db.Model):
    """ Stock's table """
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    Stock_node_id = db.Column(db.Integer)
    node = db.Column(Boolean, nullable=False, default=True)
    leaf = db.Column(Boolean, nullable=False, default=True)
    slug = db.Column(db.String())

    def __init__(self, name, color, Stock_node_id, node, leaf):
        self.name = name
        self.color = color
        self.Stock_node_id = Stock_node_id
        self.node = node
        self.leaf = leaf

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)

class People (db.Model):
    """ People's table """
    __tablename__ = 'people'

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url_image = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    cpf = db.Column(db.String, unique=True)
    phone =  Column(String, nullable=True)
    address = Column(String, nullable=True)
    people_join_date= Column(DateTime, default=func.now())
    slug = db.Column(db.String())
    # category provisoria
    category = db.Column(db.String())
    # # Associations
    # category_id = Column(Integer,
    #                     ForeignKey("category.id"), nullable=False)
    # category = relationship("Category", foreign_keys=[category_id],
    #                            backref=backref(
    #                                "people",
    #                                cascade="all, delete-orphan"))


    def __init__(self, name, email, cpf, category, phone, address):
        self.name = name
        self.email = email
        self.cpf = cpf
        self.category = category
        self.phone = phone
        self.address = address


    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)

class Customer (People):
    """ Customer's table """
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    # Associations
    people_id = Column(Integer,
                        ForeignKey("people.id"), nullable=False)
    people = relationship("People", foreign_keys=[people_id],
                               backref=backref(
                                   "customers",
                                   cascade="all, delete-orphan"))
    def __init__(self, name, email, cpf, category, phone, address):
        super().__init__(name, email, cpf, category, phone, address)


class Seller (People):
    """ Seller's table """
    __tablename__ = 'sellers'
    id = db.Column(db.Integer, primary_key=True)
    # Associations
    people_id = Column(Integer,
                        ForeignKey("people.id"), nullable=False)
    people = relationship("People", foreign_keys=[people_id],
                               backref=backref(
                                   "seller",
                                   cascade="all, delete-orphan"))
    def __init__(self):
        super().__init__()

class Product (db.Model):
    """ Product table """
    __tablename__ = 'products'

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    quantity = db.Column(db.Integer)
    purchase_price = Column(db.Float)
    sale_price = Column(db.Float)
    minimum_in_stock = db.Column(db.Integer)
    url_image = db.Column(db.String)
    activate = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())
    slug = db.Column(db.String())

    # provisorio
    category = db.Column(db.String())
    stock = db.Column(db.String())

    # Associations
    # category_id = Column(Integer,
    #                     ForeignKey("category.id"), nullable=False)
    # category = relationship("Category", foreign_keys=[category_id],
    #                            backref=backref(
    #                                "product",
    #                                cascade="all, delete-orphan"))

    # Associations
    # stock_id = Column(Integer,
    #                     ForeignKey("stock.id"), nullable=False)
    # stock = relationship("Stock", foreign_keys=[stock_id],
    #                            backref=backref(
    #                                "product",
    #                                cascade="all, delete-orphan"))



    def __init__(self, name, description, quantity, purchase_price, sale_price, \
                        minimum_in_stock, url_image, category, stock):

        self.name = name
        self.description = description
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.minimum_in_stock = minimum_in_stock
        self.url_image = url_image
        self.category = category
        self.stock = stock
        # self.category_id = 0
        # self.stock_id = 0


    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)

class Payment(db.Model):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    payment_type = Column(String(100), unique=True)
    # relationship
    # payment_bills = relationship('Payment', back_populates='payment')

class PaymentItems(db.Model):
    __tablename__ = 'payment_items'

    id = Column(Integer, primary_key=True)
    sale_id = Column(ForeignKey('sales.id'))
    payment_id = Column(ForeignKey('payments.id'))
    payment_value = Column(Float, nullable=False)
    payment_time_stamp = Column(DateTime, default=func.now())

    # relationships
    # sale = relationship('Sale', back_populates='items')
    # payment = relationship('Payment', back_populates='paymnets')

class Sale (db.Model):
    """ Sale's table """
    __tablename__ = 'sales'
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    total_price = Column(Float, nullable=False)
    sale_description = Column(String(500), default='Description Not Available')
    on_site = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=func.now())

    # # Associations
    # # sale_items
    # sale_items_id = Column(Integer,
    #                     ForeignKey("sale_items.id"), nullable=False)
    # sale_items = relationship("SaleItems", foreign_keys=[sale_items_id],
    #                            backref=backref(
    #                                "sale",
    #                                cascade="all, delete-orphan"))
    # # customer
    # customer_id = Column(Integer,
    #                     ForeignKey("customers.id"), nullable=False)
    #
    # customer = relationship("Customer", foreign_keys=[customer_id],
    #                            backref=backref(
    #                                "sale",
    #                                cascade="all, delete-orphan"))
    # # seller
    # seller_id = Column(Integer,
    #                     ForeignKey("sellers.id"), nullable=False)
    #
    # seller = relationship("Seller", foreign_keys=[seller_id],
    #                            backref=backref(
    #                                "sale",
    #                                cascade="all, delete-orphan"))
    #
    # # payment
    # payment_id = Column(Integer,
    #                     ForeignKey("payments.id"), nullable=False)
    #
    # payment = relationship("Payment", foreign_keys=[payment_id],
    #                            backref=backref(
    #                                "sale",
    #                                cascade="all, delete-orphan"))


    def __unicode__(self):
        return self.id

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)

class SaleItems(db.Model):
    __tablename__ = 'sale_items'

    id = Column(Integer, primary_key=True)
    sale_id = Column(ForeignKey('sales.id'))
    product_id = Column(ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False, default=1)
    order_price = Column(Float, nullable=False)
    order_time_stamp = Column(DateTime, default=func.now())

    # # relationships
    # sale = relationship('Sale', back_populates='sale_items')
    # # product = relationship('Product', back_populates='sale_items')

class Purchase (db.Model):
    """ Purchase's table """
    __tablename__ = 'purchases'
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    total_price = Column(Float, nullable=False)
    purchase_description = Column(String(500), default='Description Not Available')
    on_site = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=func.now())

    # # Associations
    # # purchase_items
    # purchase_items_id = Column(Integer,
    #                     ForeignKey("purchase_items.id"), nullable=False)
    # purchase_items = relationship("PurchaseItems", foreign_keys=[purchase_items_id],
    #                            backref=backref(
    #                                "purchase",
    #                                cascade="all, delete-orphan"))
    # # customer
    # customer_id = Column(Integer,
    #                     ForeignKey("customers.id"), nullable=False)
    #
    # customer = relationship("Customer", foreign_keys=[customer_id],
    #                            backref=backref(
    #                                "purchase",
    #                                cascade="all, delete-orphan"))
    # # seller
    # seller_id = Column(Integer,
    #                     ForeignKey("sellers.id"), nullable=False)
    #
    # seller = relationship("Seller", foreign_keys=[seller_id],
    #                            backref=backref(
    #                                "purchase",
    #                                cascade="all, delete-orphan"))
    #
    # # payment
    # payment_id = Column(Integer,
    #                     ForeignKey("payments.id"), nullable=False)
    #
    # payment = relationship("Payment", foreign_keys=[payment_id],
    #                            backref=backref(
    #                                "purchase",
    #                                cascade="all, delete-orphan"))
    #

    def __unicode__(self):
        return self.id

    def __repr__(self):
        return '<Instance {}: {}>'.format(self.__class__, self.id)

class PurchaseItems(db.Model):
    __tablename__ = 'purchase_items'

    id = Column(Integer, primary_key=True)
    purchase_id = Column(ForeignKey('purchases.id'))
    product_id = Column(ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False, default=1)
    order_price = Column(Float, nullable=False)
    order_time_stamp = Column(DateTime, default=func.now())

    # # relationships
    # purchase = relationship('Purchase', back_populates='items')
    # product = relationship('Product', back_populates='purchases')
