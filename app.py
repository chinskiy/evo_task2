import json
import random

from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('main.html')


@app.route("/returnAnswer", methods=['POST'])
def returnAnswer():
    print request.values
    user = request.form['textinput']
    return json.dumps({'word': random.choice(d).decode('utf-8'),
                       'user': user})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    with open('dictionary.txt') as f:
        d = f.readlines()
    app.run()
