from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'send me all your memes!'

if __name__ == "__main__":
    app.run()