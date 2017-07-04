from flask import Flask, request, send_from_directory, render_template
from flaskext.markdown import Markdown

app = Flask(__name__, static_url_path='')
Markdown(app)

@app.route('/')
def main():
    return app.send_static_file('index.html')

# static files routing

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


# dynamic views routing

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



if __name__ == '__main__':
    app.run()