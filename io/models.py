from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Chat(db.Model):
    __tablename__ = 'chat'
    chat_id       = db.Column(db.String(10), primary_key=True)
    token         = db.Column(db.String(32), unique=True, nullable=False)
    revoked       = db.Column(db.Boolean(),  unique=False, nullable=False, default=False)

    def __repr__(self):
        return '<Chat %s>' % (self.chat_id)