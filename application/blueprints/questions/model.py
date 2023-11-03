from flask import current_app
from application import db

class Questions(db.Model):
    __tablename__="questions"
    id = db.Column(db.Integer, primary_key=True)
    difficulty = db.Column(db.String(20), nullable=False)
    question = db.Column(db.String(200), nullable=False)
    answers = db.Column(db.String(300), nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Users(id: {self.id}, difficulty: {self.difficulty}, question: {self.question}, answers: {self.answers}, correct_answer: {self.correct_answer})"
    
    @property
    def json(self):
        return { "id":self.id,"difficulty":self.difficulty,"question":self.question,"answers":self.answers,"correct_answer":self.correct_answer}