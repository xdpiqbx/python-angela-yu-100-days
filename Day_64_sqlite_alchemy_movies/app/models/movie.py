import sqlalchemy as sa
from app.extensions import db


class Movie(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(250), nullable=False)
    year = sa.Column(sa.Integer)
    description = sa.Column(sa.String(1000), unique=True, nullable=False)
    rating = sa.Column(sa.Float)
    ranking = sa.Column(sa.Integer)
    review = sa.Column(sa.String(500))
    img_url = sa.Column(sa.String(500), unique=True, nullable=False)
