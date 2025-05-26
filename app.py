from flask import Flask, render_template, request, jsonify
from dao import MongoDao
from bson.objectid import ObjectId

app = Flask(__name__, static_folder="static", static_url_path="/static")
dao = MongoDao()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/items", methods=["GET"])
def get_items():
    items = dao.get_all_items()
    return jsonify(items)

@app.route("/api/items", methods=["POST"])
def add_item():
    data = request.get_json()
    name = data.get("name", "").strip()
    description = data.get("description", "").strip()
    if not name:
        return jsonify({"error": "Name is required"}), 400
    item_id = dao.add_item(name, description)
    return jsonify({"_id": str(item_id), "name": name, "description": description}), 201

@app.route("/api/items/<item_id>", methods=["GET"])
def get_item(item_id):
    item = dao.get_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

@app.route("/api/items/<item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    name = data.get("name", "").strip()
    description = data.get("description", "").strip()
    if not name:
        return jsonify({"error": "Name is required"}), 400
    updated = dao.update_item(item_id, name, description)
    if not updated:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"_id": item_id, "name": name, "description": description})

@app.route("/api/items/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    deleted = dao.delete_item(item_id)
    if not deleted:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
