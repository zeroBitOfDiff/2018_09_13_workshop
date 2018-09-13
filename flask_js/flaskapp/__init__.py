import os

from flask import Flask


# def create_app(test_config=None):
#     app = Flask(__name__)

#     @app.route('/hello')
#     def hello():
#         return 'sup'
#     from flaskapp import auth, views
#     app.register_blueprint(views.bp)
#     # app.register_blueprint(auth.bp)
#     # app.add_url_rule('/', endpoint='index')
#     return app

app = Flask(__name__)

from flaskapp import views

