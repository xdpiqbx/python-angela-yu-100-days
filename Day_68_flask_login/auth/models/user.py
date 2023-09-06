import sqlalchemy as sa
from auth.extensions import auth_db as db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class User(UserMixin, db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(100), unique=True)
    password = sa.Column(sa.String(100))
    name = sa.Column(sa.String(1000))
