from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# MongoDB connection
mongo_uri = f"mongodb+srv://natelee:{os.getenv('DB_PASSWORD')}@maxiroe-db.fr17y.mongodb.net/maxiroe-db?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client.maxiroe_db  # Your database name here

@app.route('/')
def home():
    return render_template('index.html')  # Render the home page

if __name__ == '__main__':
    app.run(debug=True)
