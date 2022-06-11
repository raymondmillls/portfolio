from flask import Flask, render_template, request
app = Flask(__name__)

common = {
    'first_name': 'Raymond',
    'last_name': 'Mills',
    'alias': ''
}

@app.route("/")
def index():
    return render_template('home.html', common=common)
