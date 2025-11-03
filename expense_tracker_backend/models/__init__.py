from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the database instance (linked later in app.py)
db = SQLAlchemy()


class User(db.Model):
    """
    Represents a registered user in the system.
    Each user can have multiple expenses linked by user_id.
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define relationship for easy access (optional but recommended)
    expenses = db.relationship("Expense", backref="user", lazy=True)


class Expense(db.Model):
    """
    Represents an expense entry made by a user.
    """
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # ✅ fixed table name here
    date = db.Column(db.Date, default=datetime.utcnow)
    category = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
