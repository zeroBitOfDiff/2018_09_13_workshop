# from flask import ( 
#     jsonify, render_template, request, Blueprint
# ) 



# bp = Blueprint('views', __name__)



# @bp.route('/', defaults={'js': 'plain'})
# @bp.route('/<any(plain, jquery, fetch):js>')
# def index(js):
#     return render_template('{0}.html'.format(js), js=js)


# @bp.route('/add', methods=['POST'])
# def add():
#     a = request.form.get('a', 0, type=float)
#     b = request.form.get('b', 0, type=float)
#     return jsonify(result=a + b)


from flask import jsonify, render_template, request

from flaskapp import app

# plain
@app.route('/', defaults={'js': 'plain'})

# fetch
@app.route('/<any(plain, jquery, fetch):js>')
def index(js):
    return render_template('{0}.html'.format(js), js=js)

# jquery
@app.route('/add', methods=['POST'])
def add():
    a = request.form.get('a', 0, type=float)
    b = request.form.get('b', 0, type=float)
    return jsonify(result=a + b)