# Import the MongoClient class from the pymongo library to connect to MongoDB
from pymongo import MongoClient
# Import ObjectId from bson to work with MongoDB document IDs
from bson.objectid import ObjectId

# Define a class for MongoDB Data Access Object
class MongoDao:
    # Constructor to initialize the MongoDB connection
    def __init__(self):
        # Create a MongoClient to connect to the local MongoDB server
        self.client = MongoClient("mongodb://localhost:27017/")
        # Access the 'flaskdb' database
        self.db = self.client["flaskdb"]
        # Access the 'items' collection within the database
        self.collection = self.db["items"]
        # Print a message indicating successful connection
        print("MongoDB connected successfully")

    # Method to retrieve all items from the collection
    def get_all_items(self):
        # Find all documents in the collection and convert to a list
        items = list(self.collection.find())
        # Convert ObjectId to string for each item
        for item in items:
            item["_id"] = str(item["_id"])
        # Return the list of items
        return items

    # Method to retrieve a single item by its ID
    def get_item(self, item_id):
        try:
            # Find one document matching the given ObjectId
            item = self.collection.find_one({"_id": ObjectId(item_id)})
            # If item is found, convert its ObjectId to string
            if item:
                item["_id"] = str(item["_id"])
            # Return the item (or None if not found)
            return item
        except Exception:
            # Return None if an error occurs (e.g., invalid ObjectId)
            return None

    # Method to add a new item to the collection
    def add_item(self, name, description):
        # Create a dictionary for the new item
        item = {"name": name, "description": description}
        # Insert the item into the collection
        result = self.collection.insert_one(item)
        # Return the inserted item's ID
        return result.inserted_id

    # Method to update an existing item by its ID
    def update_item(self, item_id, name, description):
        try:
            # Update the document matching the given ObjectId with new values
            result = self.collection.update_one(
                {"_id": ObjectId(item_id)},
                {"$set": {"name": name, "description": description}},
            )
            # Return True if any document was modified, else False
            return result.modified_count > 0
        except Exception:
            # Return False if an error occurs (e.g., invalid ObjectId)
            return False

    # Method to delete an item by its ID
    def delete_item(self, item_id):
        try:
            # Delete the document matching the given ObjectId
            result = self.collection.delete_one({"_id": ObjectId(item_id)})
            # Return True if any document was deleted, else False
            return result.deleted_count > 0
        except Exception:
            # Return False if an error occurs (e.g., invalid ObjectId)
            return False