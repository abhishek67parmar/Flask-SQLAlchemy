import os
from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate,identity
from resources.item import Item,ItemList
from resources.user import UserRegistration
from resources.store import Store,StoreList
from resources.home import Home

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL','postgresql://postgres:aaa@localhost/Store')
app.secret_key='cool'
api = Api(app)




jwt = JWT(app,authenticate,identity) #create new endpoint /auth

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>') #http://127.0.0.1:5000/item/abhi
api.add_resource(ItemList,'/items') #http://127.0.0.1:5000/items
api.add_resource(UserRegistration,'/logon')
api.add_resource(StoreList, '/stores')
api.add_resource(Home,'/')

#
# @app.before_first_request
# def create_table():
#     db.create_all()

# @app.route('/')
# def hello():
#     return "hello world"
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run()
