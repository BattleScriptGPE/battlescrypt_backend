import os
from cryptography.fernet import Fernet



def encrypt_password(password: str):
    fernet = Fernet(os.environ["SALT"])
    hash = fernet.encrypt(password.encode())
    return hash


def decrypt_password(password: str):
    fernet = Fernet(os.environ["SALT"])
    hash = fernet.decrypt(password).decode()
    return hash