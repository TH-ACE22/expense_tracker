from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from expense_tracker_backend.models.__int__ import db
from config import config
from routes.auth import auth_bp
from routes.expenses import expenses_bp

def create_app():

    app = Flask(__name__)
    app.config.from_object(config)
    
    CORS(app, origins=config.FRONTEND_URL, supports_credentials=True)
    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(expenses_bp)

    return app



if __name__ =="__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
        app.run(debug=True)




