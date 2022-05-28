#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Sample hello world Flask app"""

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> Hello, world! </h1>"

@app.route("/products")
def products():
    product_list = ["apples", "oranges", "bananas"]
    bullet_list = "".join(
        "<li>%</li>" % product for product in product_list
        )
    return "<ul>%</ul>" % bullet_list