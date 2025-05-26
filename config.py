import os

def load_config():
    """
    Return a dict of configuration values.
    Can be overridden via environment variables.
    """
    return {
        'MONGODB_URI': os.getenv('MONGODB_URI', 'mongodb://localhost:27017/yourdb'),
        'DB_NAME':    os.getenv('DB_NAME',    'yourdb'),
    }
