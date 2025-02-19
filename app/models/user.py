from datetime import datetime
from firebase_admin import firestore, credentials, initialize_app
import time
import random
import string

cred = credentials.Certificate("secret.json")  
initialize_app(cred)

db = firestore.client()


def generate_unique_id():
    """Generate a unique ID using current time and random string"""
    timestamp = int(time.time() * 1000)
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    unique_id = f"{timestamp}_{random_str}"
    
    return unique_id



class User:
    collection = db.collection('users') 
    chat_history_collection = db.collection('chats')  

    @staticmethod
    def create_user(user_data, questionnaire_responses):
        user = {
        "personal_info": user_data,
        "questionnaire_responses": questionnaire_responses,
    }
        unique_id = generate_unique_id()
        doc_ref = User.collection.document(unique_id)  
        doc_ref.set(user)  
        return unique_id  

    @staticmethod
    def get_user(user_id):
        user_doc = User.collection.document(user_id).get()
        if user_doc.exists:
            return user_doc.to_dict()
        return None

    @staticmethod
    def get_chat_history(user_id):
        """Retrieve chat history for a user"""
        chat_doc = User.chat_history_collection.document(user_id).get()
        if chat_doc.exists:
            return chat_doc.to_dict()
        return {"user_id": user_id, "messages": []}

    @staticmethod
    def update_chat_history(user_id, messages):
        """Update chat history for a user"""
        User.chat_history_collection.document(user_id).set(
            {"user_id": user_id, "messages": messages}, merge=True
        )
        

    @staticmethod
    def update_personality_profile(user_id: str, profile: dict):
        """Update user's personality profile in the database"""
        User.collection.document(user_id).update({"personality_profile": profile})

    @staticmethod
    def get_all_users():
        """Retrieve all users from the database with only name and ID"""
        users = User.collection.stream()  
        simplified_users = []
        for user in users:
            user_data = user.to_dict()
            simplified_users.append({
                "id": user.id,
                "name": user_data.get("personal_info", {}).get("name", "Unknown")
            })
        
        return simplified_users

    @staticmethod
    def get_user_with_history(user_id):
        """Retrieve user data along with their chat history"""
        user_data = User.get_user(user_id)
        if not user_data:
            raise ValueError("User not found")

        chat_history = User.get_chat_history(user_id)
        user_data['chat_history'] = chat_history
        
        return user_data
