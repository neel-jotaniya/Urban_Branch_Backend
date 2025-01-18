AI CHAT PERSONALITY APPLICATION
=============================

Description
-----------
This is a Flask-based AI chat application that creates personalized chat experiences by analyzing user personalities through questionnaires. The application uses OpenAI's GPT-3.5 model to generate responses that match the user's communication style and personality traits.

Key Features:
- Personality-based chat responses
- User onboarding with questionnaire
- Chat history tracking
- Multiple user support
- RESTful API architecture

Installation
------------
1. Prerequisites:
   - Python 3.8+
   - Firebase

2. Environment Setup:
   ```
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Firebase Setup:
   - Create a Firebase project.
   - Enable Firestore Database in Firebase.
   - Download the Firebase Admin SDK service account key and save it as `secret.json` in the project root.

4. Environment Variables:
   Create a .env file with:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

Project Structure
------------------
```
/project_root
├── app/
│   ├── routes/          # API endpoints
│   ├── models/          # Database models
│   ├── services/        # Business logic
│   ├── constants/       # Application constants
│   └── config.py        # Configuration settings
├── requirements.txt     # Python dependencies
└── run.py               # Application entry point
```

API Endpoints
------------
1. User Management:
   - GET /users - List all users
   - GET /users/<user_id> - Get user details and chat history

2. Chat:
   - POST /chat - Send/receive chat messages
   
3. Onboarding:
   - POST /onboarding - Create new user with questionnaire responses

Running the Application
----------------------
1. Start the server:
   ```
   python run.py
   ```
2. The server will run on http://localhost:5000

Testing Features
---------------
1. User Onboarding:
   - Send POST request to /onboarding with:
     ```
     {
       "personal_info": {
         "name": "John Doe",
         "age": "25",
         "sex": "Male",
         "location": "New York",
         "education": "Bachelor's",
         "job_title": "Developer",
         "company_name": "Tech Corp"
       },
       "questionnaire_responses": [
         "answer1",
         "answer2",
         ...
         "answer15"
       ]
     }
     ```

2. Chat:
   - Send POST request to /chat with:
     ```
     {
       "user_id": "user_id_here",
       "message": "Hello!"
     }
     ```

Technical Details
----------------
1. Database:
   - Firebase Firestore for storing user data and chat history.
   - Collections: users, chat_history.

2. AI Integration:
   - Uses OpenAI's GPT-3.5-turbo model.
   - Personality analysis through LangChain.
   - Custom prompt templates for consistent responses.

3. Authentication:
   - CORS enabled for localhost
   

Assumptions
----------------------------
1. Single Firebase Firestore instance is sufficient for the application.
2. Chat history is stored separately from user data for better scalability.
3. Personality analysis is done once during onboarding.
4. 15 personality questions are required for accurate profiling.
5. GPT-3.5-turbo provides sufficient accuracy for personality matching.

