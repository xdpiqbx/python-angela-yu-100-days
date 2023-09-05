from flask import Blueprint
import blog.route_handler as handler

blog = Blueprint(
    'blog',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/blog/static'
)

url_rules = (
    ('/', handler.get_all_posts, ['GET']),
    ('/about', handler.about, ['GET']),
    ('/contact', handler.contact, ['GET']),
    ('/post/<int:post_id>', handler.show_post, ['GET']),
    ('/new_post', handler.add_new_post, ['GET', 'POST']),
    ('/edit_post/<int:post_id>', handler.edit_post, ['GET', 'POST']),
    ('/delete_post/<int:post_id>', handler.delete_post, ['GET', 'POST'])
)

for route, view_func, methods in url_rules:
    blog.add_url_rule(route, view_func=view_func, methods=methods)
