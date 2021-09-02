from app import db


class Message(db.Model):
    __tablename__ = 'usermessage'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(340))

    def __init__(self, user_name=None, email=None, message=None):
        self.user_name = user_name
        self.email = email
        self.message = message

    def __repr__(self):
        return '<User> %r' % self.user_name
