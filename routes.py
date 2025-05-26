# routes.py  # Indicates the name of the file

from flask import Flask, request, jsonify, abort  # Import necessary Flask modules
from bson.json_util import dumps, ObjectId        # Import BSON utilities for JSON serialization
from dao import MongoDao                         # Import the MongoDao class for database operations

app = Flask(__name__)                            # Create a new Flask application instance
dao = MongoDao("mongodb://localhost:27017/", "flaskdb")  # Initialize the DAO with MongoDB connection

@app.route('/api/items', methods=['GET'])        # Define a route for GET requests to /api/items
def get_items():
    items = dao.read_all()                       # Retrieve all items from the database
    return jsonify(items), 200                   # Return the items as JSON with HTTP 200 status

def register_api_routes(app):                    # Define a function to register API routes
    @app.route('/api/items', methods=['GET'])    # Route for GET requests to /api/items
    def get_items():
        items = dao.find_all()                   # Retrieve all items using DAO
        return dumps(items), 200                 # Return items serialized with BSON dumps

    @app.route('/api/items/<string:item_id>', methods=['GET'])  # Route for GET requests to a specific item
    def get_item(item_id):
        item = dao.find_by_id(item_id)           # Find an item by its ID
        if not item:                             # If item not found
            abort(404)                           # Return HTTP 404 Not Found
        return dumps(item), 200                  # Return the item serialized with BSON dumps

    @app.route('/api/items', methods=['POST'])   # Route for POST requests to create a new item
    def create_item():
        data = request.json                      # Get JSON data from the request
        if not data or not data.get('name'):     # Validate that 'name' field exists
            abort(400, description="Missing 'name' field")  # Return HTTP 400 Bad Request
        item = dao.create(data)                  # Create a new item in the database
        return dumps(item), 201                  # Return the created item with HTTP 201 Created

    @app.route('/api/items/<string:item_id>', methods=['PUT'])  # Route for PUT requests to update an item
    def update_item(item_id):
        data = request.json                      # Get JSON data from the request
        if not data:                             # If no data provided
            abort(400)                           # Return HTTP 400 Bad Request
        item = dao.update(item_id, data)         # Update the item in the database
        if not item:                             # If item not found
            abort(404)                           # Return HTTP 404 Not Found
        return dumps(item), 200                  # Return the updated item

    @app.route('/api/items/<string:item_id>', methods=['DELETE'])  # Route for DELETE requests to delete an item
    def delete_item(item_id):
        dao.delete(item_id)                      # Delete the item from the database
        return '', 204                           # Return HTTP 204 No Content
