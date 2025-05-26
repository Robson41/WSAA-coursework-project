# WSAA-coursework-project
Flask Items Manager App

This is a simple full-stack web application built with Flask, MongoDB, and vanilla JavaScript that allows users to create, read, update, and delete items.

Features

Backend REST API with Flask to manage items stored in MongoDB
CRUD operations: Add, list, update, and delete items
Frontend form with validation and dynamic item list display
User-friendly messages for success and error feedback
Separate DAO layer (dao.py) for MongoDB interaction
Uses MongoDB's ObjectId for unique item IDs
Vanilla JavaScript for frontend interactivity (no frameworks)
Runs locally on port 5001 by default
Requirements

Python 3.x
MongoDB (local instance)
Python packages (install via pip):
Flask
pymongo
bson
Installation and Setup

Clone the repository
git clone <repository-url>
cd <repository-folder>
Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install Python dependencies
pip install Flask pymongo bson
Make sure MongoDB is running locally
By default, the app connects to mongodb://localhost:27017/
Ensure MongoDB service is started (mongod)
Run the Flask app
python app.py
Open your browser and go to
http://127.0.0.1:5001/
Project Structure

.
├── app.py                # Main Flask app and API endpoints
├── dao.py                # Data Access Object for MongoDB operations
├── templates/
│   └── index.html        # HTML template for frontend UI
├── static/
│   └── js/
│       └── app.js        # Frontend JavaScript for interactivity
├── README.md             # This file
How to Use

Use the form to add new items (name is required).
Items will appear in the list below the form.
Click Edit next to an item to load it into the form for editing.
Click Delete to remove an item (confirmation required).
When editing, submit updates the item instead of creating new.
Messages appear briefly to indicate success or errors.
Notes

Backend validates the name field to prevent empty entries.
Frontend performs the same validation before sending data.
MongoDB stores items with name and description fields.
IDs are handled using MongoDB's ObjectId and converted to string for JSON.

Research - Sources
Throughout the development of this project, all technical information, code examples, and troubleshooting guidance were provided via AI assistance (ChatGPT). The AI sourced and distilled content from official documentation and trusted online resources to support the implementation and resolve challenges.

Key underlying sources referenced by the AI include:

MongoDB Shell Documentation — for database interactions.
https://www.mongodb.com/docs/mongodb-shell/
Flask Official Documentation — for backend API development.
https://flask.palletsprojects.com/
JavaScript Fetch API (MDN Web Docs) — for frontend asynchronous calls.
https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

I also used AI tools (ChatGPT) to help generate, debug, and optimise code snippets, especially for integrating MongoDB with Flask, and frontend JavaScript for dynamic updates.
