import time

from werkzeug.utils import redirect

from flask import templating, request, session

from flask.ext.login import login_required, login_user, logout_user, current_user

from app import app
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    ts1 = time.strftime('%H:%M:%S', time.gmtime())
    # time.sleep(3)
    ts2 = time.strftime('%H:%M:%S', time.gmtime())

    # return "Hello, Flask!" + ts1 + " -> " + ts2
    return templating.render_template('index.html', page={
        'title': 'Index page'
    })

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')

        if username == 'user' and password == '12345':
            login_user(User(1))
            return redirect('/')

    return templating.render_template('login.html', page={
        'title': 'Login page'
    })

@app.route("/logout")
# @login_required
def logout():
    logout_user()
    session.clear()

    return redirect('/')