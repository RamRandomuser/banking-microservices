from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database connection URL (replace with your RDS endpoint, username, and password)
DATABASE_URL = "mysql+pymysql://admin:Bankappdev25@bank-app-db.c5uw8so8cf26.ap-southeast-2.rds.amazonaws.com:3306/bank_app"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    session = SessionLocal()
    new_user = User(username=data['username'], email=data['email'])
    session.add(new_user)
    session.commit()
    session.close()
    return jsonify({"message": f"User {data['username']} registered successfully!"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return jsonify({"users": [{"username": user.username, "email": user.email} for user in users]}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
