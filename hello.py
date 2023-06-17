"""estudos a partir da documentaçao do Flask 
https://flask.palletsprojects.com/en/2.3.x/"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#@app.route("/")
#def hello_world():
#    return "<p>Hello World</p>"

#conhecendo escape



#@app.route("/<name>")
#def hello(name):
#    return f"Hello, {escape(name)}!"

# conhecendo route 

@app.route("/")
def index():
    return "Index Page"

@app.route("/hello")
def hello():
    return "Hello World"

#regras de variaveis 

@app.route("/user/<username>")
def show_user_profile(username):
    #mostra o perfil daquele usuario
    return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    #mostra o post com a id informada, a id é um inteiro
    return f"Post {post_id}"

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    #mostra um outro path abaixo do path
    return f"Subpath {escape(subpath)}"

"""URLs únicas / Comportamento de Redirecionamento

As duas regras a seguir diferem em seu uso de uma barra final."""

@app.route("/projects/")
def projects():
    return "the project page"

@app.route("/about")
def about():
    return "The about page."