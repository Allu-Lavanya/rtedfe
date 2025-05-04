from pymongo import MongoClient

# Replace with your MongoDB URI
MONGO_URI = "mongodb+srv://admin:Brindavan%402004@feedbackdb.4ch4ult.mongodb.net/"

try:
    client = MongoClient(MONGO_URI)
    print("MongoDB Connection Successful!")
    # Optionally, try a test query to ensure the database and collection are accessible
    db = client['FeedbackDB']
    collection = db['feedbacks']
    print("Connected to the 'feedbacks' collection.")
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
