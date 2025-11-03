from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime



# This will be linked to the Flask app in your main file
db =SQLAlchemy()

class User(db.Model):
    """
    Represents a registered user in the system.
    Each user can have multiple expenses linked by user_id.
    """
  
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password_hash = db.Column(db.String(200), nullable= False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)


 # Optional: You can define relationship to access user.expenses easily
    # expenses = db.relationship("Expense", backref="user", lazy=True)


class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    date = db.Column(db.Date,default= datetime.utcnow)
    category = db.Column(db.String(80), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    amount = db.Column(db.Float, nullable = False)
    


