# views.py
import flask

from . import app # The directory where the file is currently (here is app/)

from .models import products


@app.route("/")
@app.route("/home")
def index():
    return flask.render_template("index.html", title="My awesome app", title2="Awesome app")

@app.route("/products")
def products_list():
    return flask.render_template("products_list.html", products=products)

@app.route("/search/by-name/<name>")
def product_page(name):
    new_list = []
    for product in products:
        if product['title'].lower() == name.lower():
            new_list.append(product)
    if not new_list:
        return "Category not found"   
    return flask.render_template("products_list.html",products =new_list )

        
@app.route("/search/by-category/<category>")
def list_by_category(category):
    new_list = [ ]
    for product in products:
        if product['category'].lower() == category.lower(): 
              new_list.append(product)
    if not new_list:
        return "Product not found"
    return flask.render_template("products_list.html", products=new_list)

@app.route("/search/by-id/<int:id_num>")
def product_by_id(id_num):
    for product in products:
        if product['id'] == id_num:
            break
    else:
        return "Product not found"
    return flask.render_template("product_page.html", product = product)

