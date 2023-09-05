from flask import render_template, redirect
from blog.repositories import posts_repo
from blog.DTO.post_dto import PostDTO
from blog.forms_wtf import AddEditPost
from blog.constants import Const


def get_all_posts():
    posts = list(posts_repo.all_posts())
    return render_template(
        Const.INDEX_HTML,
        all_posts=posts,
        bg_img=Const.HOME_BG_IMG
    )


def show_post(post_id):
    requested_post = posts_repo.post_by_id(post_id)
    requested_post.img_url = requested_post.img_url if requested_post.img_url else Const.DEFAULT_SPASE_BG_IMG
    return render_template(
        Const.POST_HTML,
        post=requested_post
    )


def add_new_post():
    form = AddEditPost()
    if form.validate_on_submit():
        new_post = PostDTO(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.content.data,
            author=form.author.data,
            img_url=form.url_bg_img.data,
        )
        posts_repo.add_new_post(new_post)
        return redirect('/')
    return render_template(
        Const.MAKE_POST_HTML,
        bg_img=Const.EDIT_BG_IMG,
        form=form
    )


def edit_post(post_id):
    post_to_edit = posts_repo.post_by_id(post_id)

    form = AddEditPost(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        author=post_to_edit.author,
        url_bg_img=post_to_edit.img_url,
        content=post_to_edit.body
    )

    if form.validate_on_submit():
        post = PostDTO(
            id=post_id,
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.content.data,
            author=form.author.data,
            img_url=form.url_bg_img.data,
        )
        posts_repo.edit_post(post)
        return redirect(f"/post/{post_id}")

    return render_template(
        Const.MAKE_POST_HTML,
        bg_img=post_to_edit.img_url if post_to_edit.img_url else Const.EDIT_BG_IMG,
        form=form,
        is_edit=True
    )


def delete_post(post_id):
    posts_repo.delete_post_by_id(post_id)
    return redirect('/')


def about():
    return render_template(
        Const.ABOUT_HTML,
        bg_img=Const.ABOUT_BG_IMG
    )


def contact():
    return render_template(
        Const.CONTACT_HTML,
        bg_img=Const.CONTACT_BG_IMG
    )
