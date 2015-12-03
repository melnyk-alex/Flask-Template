from datetime import timedelta
from flask import Flask, session
from flask.ext.login import LoginManager
from flask.sessions import SessionInterface

app = Flask(__name__)
app.config.from_object('config')
# Additional frameworks
lm = LoginManager(app)

class BeakerSession(SessionInterface):
    def open_session(self, app, request):
        session = request.environ['beaker.session']
        return session

    def save_session(self, app, session, response):
        return session.save()


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=120)

from app import views, auth