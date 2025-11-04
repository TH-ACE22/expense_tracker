import os



class Config:
  # Flask secret key (for session and JWT)
  SECRET_KEY = os.environ.get("SECRET_KEY", " supersecret")

  #PostgresQL database configuration

  SQLALCHEMY_DATABASE_URI = os.environ.get(
     "DATABASE_URL",
     "postgresql://postgres:food@localhost:5432/expense" 

 )
  SQLALCHEMY_TRACK_MODIFICATIONS = False



  # The frontEnd  URL allowed to connect

  FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:5173")

