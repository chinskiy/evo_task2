import json
import random
import sqlite3
import os.path

from flask import Flask
from flask import render_template
from flask import request


if not os.path.isfile('database.db'):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE users(user text, epithet text)''')
    conn.commit()
    conn.close()


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('main.html')


@app.route("/returnAnswer", methods=['POST'])
def returnAnswer():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    user = request.form['textinput']

    epith = c.execute('''SELECT epithet FROM users 
                                        WHERE user=?''', (user,)).fetchone()
    if epith is None:
        with open('dictionary.txt') as f:
            d = f.readlines()
        epith = random.choice(d).decode('utf-8')
        c.execute("INSERT INTO users VALUES (?, ?)", (user, epith, ))
        conn.commit()
    conn.close()
    return json.dumps({'word': epith,
                       'user': user})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run()
