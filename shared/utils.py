import bcrypt

def hash_password(password):
    """Hash a plaintext password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plaintext, hashed):
    """Verify a plaintext password against the hashed password."""
    return bcrypt.checkpw(plaintext.encode('utf-8'), hashed.encode('utf-8'))
