from flask import Flask, session, request, redirect, url_for
from utils.db_functions import is_registered, get_user_items

import json

app = Flask(__name__)

app.secret_key = b'12345'

@app.route('/', methods=['GET'])
def index():

    if 'username' in session:
        return f'Logged in as <strong>{session["username"]}</strong>'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if is_registered(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return '''
        <form method="post">
            <p>username<input type=text name=username>
            <p>password<input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/item')
def item():
    if 'username' in session:
        items = get_user_items(session['username'])
        return json.dumps({
            "items": items
        })
    return 'No items to show. You are not logged in.'


if __name__ == '__main__':
    app.run()