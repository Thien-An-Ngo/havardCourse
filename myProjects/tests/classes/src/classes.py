from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Awakened(db.Model):
    __tablename__ = "awakened"
    id = db.Column(db.Integer, primary_key=True)
