import sqlalchemy as sa
from blog.extensions import blog_db as db


class BlogPost(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(250), unique=True, nullable=False)
    subtitle = sa.Column(sa.String(250), nullable=False)
    date = sa.Column(sa.String(250), nullable=False)
    body = sa.Column(sa.Text, nullable=False)
    author = sa.Column(sa.String(250), nullable=False)
    img_url = sa.Column(sa.String(250), nullable=True)
