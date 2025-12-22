from motor.motor_asyncio import AsyncIOMotorClient

class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient("mongodb://localhost:27017")
        self.db = self.client["workout_db"]

db = MongoDB().db