import os

from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
 

    Bootstrap(app)

    # register the database commands
    # from flaskapp import db
    # db.init_app(app)

    # apply the blueprints to the app
    from flaskapp import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule('/', endpoint='index')

    return app