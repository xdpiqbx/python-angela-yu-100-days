from flask import Blueprint
import auth.route_handler as handler
from flask_login import login_required

auth = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/auth/static'
)

url_rules = (
    ('/', handler.home, ['GET']),
    ('/register', handler.register, ['GET', 'POST']),
    ('/login', handler.login, ['GET', 'POST']),
    ('/secrets', login_required(handler.secrets), ['GET']),
    ('/logout', login_required(handler.logout), ['GET']),
    ('/download', login_required(handler.download), ['GET']),
)

for route, view_func, methods in url_rules:
    auth.add_url_rule(route, view_func=view_func, methods=methods)
