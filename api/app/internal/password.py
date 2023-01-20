import base64

def encrypt_password(password: str):
    password = password.encode("utf-8")
    password = base64.b64encode(password)
    return password