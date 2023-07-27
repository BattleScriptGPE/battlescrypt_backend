import os
import crypt



def encrypt_password(password: str):
    hash = crypt.crypt(password, os.environ["SALT"])
    return hash
