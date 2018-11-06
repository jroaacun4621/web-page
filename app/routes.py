from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html'
    )

@app.route('/subscription')
def subscription():
    return render_template(
        'subscription.html'
    )

@app.route('/experience')
def experience():
    return render_template(
        'workexperience.html'
    )