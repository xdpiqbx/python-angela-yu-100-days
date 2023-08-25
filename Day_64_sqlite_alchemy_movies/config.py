import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'movies.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Default value = None
