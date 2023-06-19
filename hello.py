"""estudos a partir da documentaçao do Flask 
https://flask.palletsprojects.com/en/2.3.x/"""

from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

app = Flask(__name__)

#@app.route("/")
#def hello_world():
#    return "<p>Hello World</p>"

#conhecendo escape



#@app.route("/<name>")
#def hello(name):
#    return f"Hello, {escape(name)}!"

# conhecendo route 
"""
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

"""

"""URLs únicas / Comportamento de Redirecionamento

As duas regras a seguir diferem em seu uso de uma barra final."""
"""
@app.route("/projects/")
def projects():
    return "the project page"

@app.route("/about")
def about():
    return "The about page."

"""
#URL Building
"""
@app.route("/")
def index():
    return "index"

@app.route("/login")
def login():
    return "login"

@app.route("/user/<username>")
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username = "Renan Neves"))
"""

#http methods

"""Aplicações web utilizam diferentes métodos HTTP ao acessar URLs. 
É importante se familiarizar com os métodos HTTP ao trabalhar com Flask. 
Por padrão, uma rota responde apenas a solicitações GET. 
Você pode usar o argumento methods do decorador route() para lidar com diferentes métodos HTTP."""

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()
    
"""O exemplo acima mantém todos os métodos da rota dentro de uma única função, o que pode ser útil se cada parte utilizar alguns dados comuns.
Você também pode separar as visualizações para diferentes métodos em funções diferentes. 
O Flask fornece um atalho para decorar essas rotas com get(), post(), etc., para cada método HTTP comum.
"""

app.get("/login")
def login_get():
    return show_the_login_form()

app.post("/login")
def login_post():
    return do_the_login()