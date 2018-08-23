from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Chat(db.Model):
    id          = db.Column(db.String(10), primary_key=True)
    uuid        = db.Column(db.String(32), unique=True, nullable=False)
    revoked     = db.Column(db.Boolean(),  unique=True, nullable=False, default=False)

    def __repr__(self):
        return '<User %r>' % self.username