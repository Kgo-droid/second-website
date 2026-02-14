from flask import Flask


def create_app():

    app = Flask(__name__)
    app.config['SECRET KEY'] = 'bendania2004'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
