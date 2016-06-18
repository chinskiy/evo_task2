from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('main.html')


@app.route("/returnAnswer", methods=['POST'])
def returnAnswer():
    print request.values
    user = request.form['textinput']
    #return json.dumps({'status':'OK','user':user})
    return json.dumps({'status':'OK','user': 'hallo ' + user})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
