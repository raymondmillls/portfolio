from flask import Flask
app = Flask(__name__)

common = {
    'first_name': 'Raymond',
    'last_name': 'Mills',
    'alias': ''
}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
