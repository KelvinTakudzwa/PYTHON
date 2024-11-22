import hashlib

passwords = {}

def hash_password(password):
    # Use a suitable hashing algorithm (e.g., SHA256) to hash the password
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.hexdigest()
    return hashed_password

def store_password(username, password):
    # Hash the password
    hashed_password = hash_password(password)

    # Store the hashed password in the dictionary
    passwords[username] = hashed_password

def check_password(username, password):
    # Retrieve the hashed password from the dictionary
    hashed_password = passwords.get(username)

    if hashed_password is None:
        return False

    # Hash the input password and compare it with the stored hashed password
    return hash_password(password) == hashed_password