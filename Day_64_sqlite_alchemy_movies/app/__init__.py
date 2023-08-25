from flask import Flask
from app.main import bp as main_bp
from app.extensions import db, bootstrap5

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    bootstrap5(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register blueprints here
    app.register_blueprint(main_bp)

    print(db)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
