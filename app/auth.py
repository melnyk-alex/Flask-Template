from werkzeug.utils import redirect

from app import lm
from app.models import User

@lm.unauthorized_handler
def returnToLogin():
    return redirect('/login')


@lm.user_loader
def user_loader(id):
    return User(id) if id else None