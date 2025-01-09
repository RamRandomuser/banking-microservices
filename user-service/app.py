from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    # Simulate user registration (later, link this to your database)
    return jsonify({"message": f"User {data['username']} registered successfully!"}), 201
  
@app.route('/users', methods=['GET'])
def get_users():
    # Simulate fetching users from database
    users = [
        {"username": "alice", "email": "  [email protected] "}, 
        {"username": "bob", "email": "  [email protected] "}        
    ]
    return jsonify({"users": users}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)