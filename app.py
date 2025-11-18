from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)



@app.route("/")
@app.route("/<p>")
def index(p=None):
    if p is None:
        p="Default"
    url_for('static', filename='index.css')
    return render_template('index.html', person=p)

@app.route('/about')
def about():
    return 'The about page'

@app.route('/health')
def healthcheck():
    return 'The about page'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('index', namee="Flask"))
    print(url_for('about'))
    print(url_for('healthcheck'))