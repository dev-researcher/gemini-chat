from flask import Flask

def create_app():
    app = Flask(_name_)
    app.config.from_pyfile('config.py')

    from .routes import main
    app.register_blueprint(main)

    return app