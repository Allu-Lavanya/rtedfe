from pymongo import MongoClient

# Replace with your MongoDB URI
MONGO_URI = "mongodb+srv://Allu-Lavanya:fx-991EX@cluster0.lei6zc4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(MONGO_URI)
    print("MongoDB Connection Successful!")
    # Optionally, try a test query to ensure the database and collection are accessible
    db = client['FeedbackDB']
    collection = db['feedbacks']
    print("Connected to the 'feedbacks' collection.")
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
