from flask import Flask 
from flask_cors import CORS  # type: ignore # Enables cross-origin requests (used with frontend apps)
from flask_jwt_extended import JWTManager  # type: ignore # For handling JWT-based authentication
from models import db # Import the SQLAlchemy db instance (fixed typo from __int__)
from config import Config  # Import app configuration (e.g., database URI, secret key)
from routes.auth import auth_bp  # Import the authentication routes blueprint
from routes.expenses import expense_bp  # Import the expenses routes blueprint (fixed variable name)

# ===========================
# APP FACTORY FUNCTION
# ===========================
def create_app():


 
    """
    Application factory that creates and configures the Flask app.
    This pattern allows flexibility for testing, scaling, and cleaner code organization.
    """
    app = Flask(__name__)

    # Load configuration settings (from config.py)
    app.config.from_object(Config)

    # Enable Cross-Origin Resource Sharing for the frontend (React, etc.)
    # This allows frontend requests (e.g., http://localhost:5173) to reach your Flask API
    CORS(app, origins=Config.FRONTEND_URL, supports_credentials=True)

    # Initialize database with Flask app
    db.init_app(app)

    # Initialize JWT for authentication management
    JWTManager(app)

    # Register blueprints (modular route groups)
    app.register_blueprint(auth_bp)      # Handles /auth routes (register, login)
    app.register_blueprint(expense_bp)   # Handles /expenses routes (add, view, delete)

    # Return the fully configured Flask app instance
    return app


# ===========================
# RUN THE APP
# ===========================
if __name__ == "__main__":
    # Create app instance
    app = create_app()

    # Use application context so db.create_all() can access app configuration
    with app.app_context():
        db.create_all()  # Creates all tables defined in your models if not already created

        # Run the app in debug mode (useful for development)
        app.run(debug=True)
