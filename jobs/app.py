from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')


def bulma():
    return redirect('static:filename:css/bulma.min.css')
