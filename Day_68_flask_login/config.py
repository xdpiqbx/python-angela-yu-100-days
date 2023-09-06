import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
blog_module_dir = os.path.join(basedir, 'auth')


class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(blog_module_dir, 'auth.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Default value = None
