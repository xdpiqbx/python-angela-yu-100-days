from flask import Flask
from auth import auth
from config import Config
from auth.extensions import auth_db, login_manager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    auth_db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        auth_db.create_all()

    app.register_blueprint(auth)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
