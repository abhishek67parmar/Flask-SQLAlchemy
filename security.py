from models.user import UserModel
from werkzeug.security import safe_str_cmp



def authenticate(username,password):
    user= UserModel.find_by_username(username)
    if user and UserModel.verify_hash(password, user.password ):
        return user

def identity(payload):
    user_id=payload['identity']
    return UserModel.find_by_id(user_id)
