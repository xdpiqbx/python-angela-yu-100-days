from blog.DTO.post_dto import PostDTO
from blog.models import BlogPost
from blog.extensions import blog_db as db
import sqlalchemy as sa


def all_posts():
    return db.session.execute(
        sa.select(BlogPost)
    ).scalars().all()


def post_by_id(post_id):
    return db.get_or_404(BlogPost, post_id)


def add_new_post(post: PostDTO):
    db.session.add(
        BlogPost(
            title=post.title,
            subtitle=post.subtitle,
            date=post.date,
            body=post.body,
            author=post.author,
            img_url=post.img_url
        )
    )
    db.session.commit()


def edit_post(post: PostDTO):
    post_to_edit: BlogPost = post_by_id(post.id)
    post_to_edit.title = post.title
    post_to_edit.subtitle = post.subtitle
    post_to_edit.date = post.date
    post_to_edit.body = post.body
    post_to_edit.author = post.author
    post_to_edit.img_url = post.img_url
    db.session.commit()


def delete_post_by_id(post_id):
    post_to_delete: BlogPost = post_by_id(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
