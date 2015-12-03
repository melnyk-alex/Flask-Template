
class User():
    anonymous = None
    active = None
    id = None

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return self.anonymous

    def get_id(self):
        return self.id

    def __init__(self, id, anonymous=False, active=True):
        self.id = id
        self.anonymous = anonymous
        self.active = active

    def __str__(self):
        return 'User #{}'.format(self.id)