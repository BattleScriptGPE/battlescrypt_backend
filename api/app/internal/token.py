import jwt
import time


JWT_SECRET = "secret"
JWT_ALGO = "HS256"

def create_token(id , name , role):
    encoded_jwt = jwt.encode({"username" : name , "role" : role , "id" : id}, JWT_SECRET,algorithm=JWT_ALGO)
    return encoded_jwt


def decode_token(token):
    decoded_jwt = jwt.decode(token , JWT_SECRET , algorithms=[JWT_ALGO])
    return decoded_jwt
