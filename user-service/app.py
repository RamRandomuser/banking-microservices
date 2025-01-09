from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import bcrypt

app = Flask(__name__)

# JWT Secret Key (should be an environment variable in production)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# Database connection URL
DATABASE_URL = "mysql+pymysql://admin:Bankappdev25@bank-app-db.c5uw8so8cf26.ap-southeast-2.rds.amazonaws.com:3306/bank_app"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # Store hashed passwords

# Create tables
Base.metadata.create_all(bind=engine)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    session = SessionLocal()

    # Check if email already exists
    existing_email = session.query(User).filter_by(email=data['email']).first()
    if existing_email:
        return jsonify({"error": "Email already registered"}), 400

    # Check if username already exists
    existing_username = session.query(User).filter_by(username=data['username']).first()
    if existing_username:
        return jsonify({"error": "Username already taken"}), 400

    # Hash the password
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    # Create a new user
    new_user = User(username=data['username'], email=data['email'], password=hashed_password.decode('utf-8'))
    session.add(new_user)
    session.commit()
    session.close()
    return jsonify({"message": f"User {data['username']} registered successfully!"}), 201


@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    session = SessionLocal()

    # Check if the user exists
    user = session.query(User).filter_by(email=data['email']).first()
    if not user:
        return jsonify({"error": "Invalid email or password"}), 401

    # Verify the password
    if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({"error": "Invalid email or password"}), 401

    # Generate JWT token
    access_token = create_access_token(identity={"username": user.username, "email": user.email})
    return jsonify({"message": "Login successful", "access_token": access_token}), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"message": "This is a protected route"}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
