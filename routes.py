# routes.py
from flask import Flask, request, jsonify, abort
from bson.json_util import dumps, ObjectId
from dao import MongoDao

app = Flask(__name__)
dao = MongoDao("mongodb://localhost:27017/", "flaskdb")

@app.route('/api/items', methods=['GET'])
def get_items():
    items = dao.read_all()  # Make sure you have a method to get all items in your DAO
    return jsonify(items), 200


def register_api_routes(app):
    @app.route('/api/items', methods=['GET'])
    def get_items():
        items = dao.find_all()
        return dumps(items), 200  # Using bson.json_util.dumps to handle ObjectId serialization

    @app.route('/api/items/<string:item_id>', methods=['GET'])
    def get_item(item_id):
        item = dao.find_by_id(item_id)
        if not item:
            abort(404)
        return dumps(item), 200

    @app.route('/api/items', methods=['POST'])
    def create_item():
        data = request.json
        if not data or not data.get('name'):
            abort(400, description="Missing 'name' field")
        item = dao.create(data)
        return dumps(item), 201

    @app.route('/api/items/<string:item_id>', methods=['PUT'])
    def update_item(item_id):
        data = request.json
        if not data:
            abort(400)
        item = dao.update(item_id, data)
        if not item:
            abort(404)
        return dumps(item), 200

    @app.route('/api/items/<string:item_id>', methods=['DELETE'])
    def delete_item(item_id):
        dao.delete(item_id)
        return '', 204
