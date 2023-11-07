from flask import current_app
from application import db

class Scoreboard(db.Model):
    __tablename__ = "scoreboard"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(200),nullable=False)
    score = db.Column(db.Integer,nullable=False)


    def __repr__(self):
        return f"Scoreboard(id: {self.id}, username: {self.username}, score: {self.score})"
    
    @property
    def json(self):
        return { "id":self.id,"username":self.username,"score":self.score }