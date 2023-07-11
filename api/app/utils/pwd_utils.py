import os

def encrypt_password(password: str):
    password = '1234$' + password
    return str(password.encode('utf-8'))

