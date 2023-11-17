from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MONGO_URI = os.environ.get('MONGO_URI')
    DATABASE_NAME = os.environ.get("DB_NAME")

    @staticmethod
    def get_database():
        client = MongoClient(Config.MONGO_URI)
        return client[Config.DATABASE_NAME]