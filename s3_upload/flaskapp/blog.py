#blog.py
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for, redirect
)
from werkzeug.exceptions import abort
#from werkzeug.utils import secure_filename
from flaskapp.s3helper import *
from flaskapp.auth import login_required
# from flaskapp.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    """Show all the posts, most recent first."""
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    return render_template('blog/index.html')

@bp.route("/", methods=["POST"])
def upload_file():

	# A
    if "user_file" not in request.files:
        return "No user_file key in request.files"

	# B
    file    = request.files["user_file"]

    """
        These attributes are also available

        file.filename               # The actual name of the file
        file.content_type
        file.content_length
        file.mimetype

    """

	# C.
    if file.filename == "":
        return "Please select a file"

	# D.
    
    if file:
        #file.filename = secure_filename(file.filename)
        output = upload_file_to_s3(file)
        return redirect("/")

    else:
        return redirect("/")
# def get_post(id, check_author=True):
#     """Get a post and its author by id.
#     Checks that the id exists and optionally that the current user is
#     the author.
#     :param id: id of post to get
#     :param check_author: require the current user to be the author
#     :return: the post with author information
#     :raise 404: if a post with the given id doesn't exist
#     :raise 403: if the current user isn't the author
#     """
#     # post = get_db().execute(
#     #     'SELECT p.id, title, body, created, author_id, username'
#     #     ' FROM post p JOIN user u ON p.author_id = u.id'
#     #     ' WHERE p.id = ?',
#     #     (id,)
#     # ).fetchone()

#     if post is None:
#         abort(404, "Post id {0} doesn't exist.".format(id))

#     if check_author and post['author_id'] != g.user['id']:
#         abort(403)

#     return post


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        # else:
        #     db = get_db()
        #     db.execute(
        #         'INSERT INTO post (title, body, author_id)'
        #         ' VALUES (?, ?, ?)',
        #         (title, body, g.user['id'])
        #     )
        #     db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    # post = get_post(id)

    # if request.method == 'POST':
    #     title = request.form['title']
    #     body = request.form['body']
    #     error = None

    #     if not title:
    #         error = 'Title is required.'

    #     if error is not None:
    #         flash(error)
    #     # else:
    #     #     db = get_db()
    #     #     db.execute(
    #     #         'UPDATE post SET title = ?, body = ? WHERE id = ?',
    #     #         (title, body, id)
    #     #     )
    #     #     db.commit()
    #         return redirect(url_for('blog.index'))

    return render_template('blog/update.html')


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    """Delete a post.
    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    # Sget_post(id)
    # db = get_db()
    # db.execute('DELETE FROM post WHERE id = ?', (id,))
    # db.commit()
    return redirect(url_for('blog.index'))