from flask_restful import Resource,reqparse
from models.user import UserModel


class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type= str,
        required = True
    )

    parser.add_argument('password',
        type= str,
        required = True
    )

    def post(self):
        data= UserRegistration.parser.parse_args()
        testuser = UserModel.find_by_username(data['username'])
        if testuser:
            return {"message": "Already exists"}

        user = UserModel(data['username'],UserModel.generate_hash(data['password']))
        user.save_to_db()


        return {"message": "User created"},201
