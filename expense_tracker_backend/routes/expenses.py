from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Expense 


expense_bp = Blueprint("expenses", __name__, url_prefix="/expenses")

@expenses_bp.route("/", methods=["GET"])
@jwt_required()

def get_expenses():
    user_id = get_jwt_identity()
    expenses = Expense/query.filter_by(user_id=user_id).all()
    return jsonify([
        {"id": e.id, "title":e.title, "amount": e.amunt, "category": e.category, "date":e.date.isoformat()}
        for e in expenses
    ])

@expenses_bp.route("/", methods=["POST"])
@jwt_required()
def add_expense():
    user_id = get_jwt_identity()
    data = request.get_json()

    expense = Expense(

        title = data["title"],
        amount = data["amount"],
        category = data["category"],
        user_id=user_id
    )
    db.session.add(expense)