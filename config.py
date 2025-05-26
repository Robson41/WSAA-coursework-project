import os

def load_config():
    """
    Return a dict of configuration values.
    Can be overridden via environment variables.
    """
    # Return a dictionary containing configuration values.
    # The values can be overridden by setting the corresponding environment variables.
    return {
        # MongoDB connection URI, defaults to local instance if not set in environment
        'MONGODB_URI': os.getenv('MONGODB_URI', 'mongodb://localhost:27017/yourdb'),
        # Database name, defaults to 'yourdb' if not set in environment
        'DB_NAME':    os.getenv('DB_NAME',    'yourdb'),
    }
