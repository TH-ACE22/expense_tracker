# Import necessary modules
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash  # fixed spelling
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity  # fixed names
from models import db, User  # import database and User model

# Create a blueprint for authentication routes
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


# ===========================
# REGISTER NEW USER
# ===========================
@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Registers a new user by saving their username and hashed password in the database.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Check if the username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    # Hash the password for security before storing it
    hashed_pw = generate_password_hash(password)

    # Create a new user record
    new_user = User(username=username, password_hash=hashed_pw)

    # Save user to database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# ===========================
# LOGIN EXISTING USER
# ===========================
@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Logs in an existing user and returns a JWT access token for authentication.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Find the user by username
    user = User.query.filter_by(username=username).first()

    # If user doesn't exist or password is incorrect
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"message": "Invalid credentials"}), 401

    # Create a JWT token containing the user's ID as identity
    access_token = create_access_token(identity=user.id)

    # Return the token and user info
    return jsonify({
        "access_token": access_token,
        "user": username
    })
