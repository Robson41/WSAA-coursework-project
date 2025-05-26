from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDao:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["flaskdb"]
        self.collection = self.db["items"]
        print("MongoDB connected successfully")

    def get_all_items(self):
        items = list(self.collection.find())
        for item in items:
            item["_id"] = str(item["_id"])
        return items

    def get_item(self, item_id):
        try:
            item = self.collection.find_one({"_id": ObjectId(item_id)})
            if item:
                item["_id"] = str(item["_id"])
            return item
        except Exception:
            return None

    def add_item(self, name, description):
        item = {"name": name, "description": description}
        result = self.collection.insert_one(item)
        return result.inserted_id

    def update_item(self, item_id, name, description):
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(item_id)},
                {"$set": {"name": name, "description": description}},
            )
            return result.modified_count > 0
        except Exception:
            return False

    def delete_item(self, item_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(item_id)})
            return result.deleted_count > 0
        except Exception:
            return False
