from flask_restful import Resource, reqparse
from flask_jwt  import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help= "This field can not be left blank"
    )

    parser.add_argument('store_id',
        type=int,
        required=True,
        help= "Required for an item"
    )

    @jwt_required()
    def get(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'No item found'},404



    def post(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            return {'message':"an item '{}' already present".format(name)},400

        data= Item.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])

        #try:
        item.save_to_db()
        # except:
            # return {"message": "Error in insertion"},500
        return item.json(),201


    def put(self,name):
        item=ItemModel.find_by_name(name)
        data=Item.parser.parse_args()
        #updated_item = ItemModel(name,data['price'],data['store_id'])
        if item is None:
            item = ItemModel(name,**data)
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        item.save_to_db()
        return item.json()

    def delete(self,name):
        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db()

        return {'message':'item {} deleted...'.format(name)}


class ItemList(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]}
