from flask_jwt_extended import JWTManager

def setup_jwt(app):
    """Set up JWT for Flask app."""
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Replace with env vars in production
    return JWTManager(app)
