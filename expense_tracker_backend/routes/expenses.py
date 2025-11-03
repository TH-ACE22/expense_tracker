# import neccessary modules from Flask and Flask_JWT_Extended
from flask import Blueprint, request, jsonify # type: ignore
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore
from models import db, Expense  #import the database and Expense model


# Define a Blueprint for expense-related routes
# This groups expenses routes under the prefix "/expenses"
expense_bp = Blueprint("expenses", __name__, url_prefix="/expenses")

#=================================
# GET /expenses/
#================================

@expense_bp.route("/", methods=["GET"]) 

@jwt_required() # Required a valid JWT Token to access this route

def get_expenses():
    # Get the currently logged in user's ID from the JWT
    user_id = get_jwt_identity()

    # Query all expenses belonging to that user

    expenses = Expense/query.filter_by(user_id=user_id).all() # type: ignore

    # Return the expenses as a JSON list
    # Each expense is represented as a dictionary

    return jsonify([
        {"id": e.id, "title":e.title, "amount": e.amount, "category": e.category, "date":e.date.isoformat()  # convert datetime to a string for JSON
         
         }
        for e in expenses
    ])


# ==================================
# POST /expense/
# ================================
@expense_bp.route("/", methods=["POST"]) 
@jwt_required()
def add_expense():
    # Get user ID from  the JWT
    user_id = get_jwt_identity()
    
    # PArse JSON data sent in the request body
    data = request.get_json()

    # Create a new Expense instance
    expense = Expense(

        title = data["title"],
        amount = data["amount"],
        category = data["category"],
        user_id=user_id
    )

    #add expenses to the database
    db.session.add(expense)
    db.session.commit()

    # Return a sucess message with HTTP status code 201(Created)
    return jsonify({"message" : "Expense added"}), 201


# ====================================
# DELETE /expenses/<id>
# ====================================
@expense_bp.route("/<int:id>",methods= ["DELETE"])
@jwt_required()
def delete_expense(id):
    # Get the user ID from the JWT
    user_id = get_jwt_identity()

    # Find teh expense that matches both the ID and user ID
    
    expense = Expense.query.filter_by(id=id, user_id=user_id).first()

    #  If the expense doen't exists , return 404
    if not expense:
        return jsonify({"message":"Expense not found"}), 404
    
    # Delete the expense from the database
    db.seession.delete(expense)
    db.session.commit()

    # Return confirmation message
    return jsonify({"message": "Expense deleted"})
    
