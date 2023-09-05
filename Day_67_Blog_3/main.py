from flask import Flask
from flask_bootstrap import Bootstrap5

from blog import blog
from config import Config
from blog.extensions import blog_db, ckeditor


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    Bootstrap5(app)
    blog_db.init_app(app)
    ckeditor.init_app(app)

    with app.app_context():
        blog_db.create_all()

    app.register_blueprint(blog)

    return app


if __name__ == "__main__":
    create_app().run(debug=True, port=5000)
