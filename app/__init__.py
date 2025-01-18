from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.routes.chat import ChatResource
from app.routes.user import UserHistoryResource, UsersResource
from app.routes.onboarding import OnboardingResource


def create_app():
    # Initialize the Flask app
    app = Flask(__name__)
    
    # Configure CORS to allow requests from specific origin
    cors_config = {
        r"/*": {
            "origins": "http://localhost:5173",  # Allow frontend origin
            "supports_credentials": True       # Allow cookies or Authorization headers
        }
    }
    CORS(app, resources=cors_config)
    
    # Initialize the Flask-RESTful API
    api = Api(app)
    
    # Add resources to the API
    api.add_resource(UsersResource, '/users')                        # Endpoint for user list
    api.add_resource(UserHistoryResource, '/users/<string:user_id>') # Endpoint for user history
    api.add_resource(ChatResource, '/chat')                          # Endpoint for chat
    api.add_resource(OnboardingResource, '/onboarding')              # Endpoint for onboarding
    
    return app

