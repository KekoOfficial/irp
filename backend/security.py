import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify(password, hashed):
    return hash_password(password) == hashed