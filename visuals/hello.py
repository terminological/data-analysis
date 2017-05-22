from flask import Flask
from flask import render_template
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

