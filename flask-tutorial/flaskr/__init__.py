import os
from flask import Flask

def create_app(test_config= None):
    #cria e configura o app
    app = Flask(__name__, instance_relative_config= True)
    app.config.from_mapping(
        SECRET_KEY= 'dev',
        DATABASE= os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # carrega a configuração da instância, se existir, quando não estiver testando
        app.config.from_pyfile('config.py', silent= True)
    else:
        #se for aprovado, carrega a configuração de teste
        app.config.from_mapping(test_config)

    #se sertifica que a pasta da instancia exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    
    return app

    #uma pagina simples que diz hello
    @app.route('/hello')
    def hello():
        return 'Hello world'
    
    return app