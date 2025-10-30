from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime

db =SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password_hash = db.Column(db.String(200), nullable= False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)




class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    date = db.Column(db.Date, nullable= False)
    category = db.Column(db.String(80), nullable = False)
    description = db.Column(db.Text)
    amount = db.Column(db.Float, nullable = False)
    created_at = db.Column(db.dateTime, default = datetime.utcnow)





