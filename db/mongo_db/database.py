from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


client = MongoClient(os.environ["MONGO_URL"])

messages_db = client["messages"]

all_messages_collection = messages_db["all_messages_collection"]
