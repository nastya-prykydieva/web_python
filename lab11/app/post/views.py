from . import post_bp
from app import db
from flask import render_template, request, redirect, url_for, flash, current_app
from .models import Post, Type
from .forms import PostForm
from flask_login import login_required, current_user
from PIL import Image
import os
import secrets


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/post_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@post_bp.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    post_list = Post.query.all()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, text=form.text.data, type=form.type.data,
                        enabled=form.enabled.data, user_id=current_user.id)
        if form.image.data:
            image = save_picture(form.image.data)
            new_post.image = image
        db.session.add(new_post)
        db.session.commit()
        flash("The new post was added successfully.", "success")
        return redirect(url_for("post_bp.list_post"))
    elif request.method != "GET":
        flash("The new task was not added!", "danger")
    return render_template('create_post.html', form=form, post_list=post_list)


@post_bp.route("/", methods=['GET'])
@login_required
def list_post():
    post_list = db.session.query(Post).all()
    return render_template('list_post.html', post_list=post_list)


@post_bp.route("/<int:id>", methods=["GET"])
@login_required
def view(id):
    post = Post.query.get_or_404(id)
    return render_template('view_post.html', post=post)


@post_bp.route("/<int:id>/update", methods=["GET", "POST"])
@login_required
def update(id):
    form = PostForm()
    post = Post.query.get_or_404(id)
    if form.validate_on_submit():
        if form.image.data:
            image = save_picture(form.image.data)
            post.image = image
        post.title = form.title.data
        post.text = form.text.data
        post.enabled = form.enabled.data
        post.type = form.type.data
        db.session.commit()
        flash(f"Post №{id} was updated.", "success")
        return redirect(url_for("post_bp.view", id=id))
    elif request.method == "GET":
        form.title.data = post.title
        form.text.data = post.text
        form.enabled.data = post.enabled
        form.type.data = post.type.name
    return render_template('update_post.html', form=form, post=post)


@post_bp.route("/<int:id>/delete", methods=['GET', 'POST'])
@login_required
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash(f"Post №{id} was deleted.", "success")
    return redirect(url_for("post_bp.list_post"))
