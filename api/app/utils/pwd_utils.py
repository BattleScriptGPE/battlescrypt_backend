import os
import hashlib

def encrypt_password(password: str):
    hash = hashlib.md5(password.encode('utf-8'))
    return hash.hexdigest()
    