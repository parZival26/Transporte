from decouple import config
import motor.motor_asyncio


CONNECTION_STRING = config('CONNECTION_STRING')
_client: motor.motor_asyncio.AsyncIOMotorClient = None
_database: motor.motor_asyncio.AsyncIOMotorDatabase = None


async def connect():
    global _client, _database
    _client = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STRING)
    _database = _client["Transporte"]
   

async def close_connection():
    global _client
    if _client:
        _client.close()

def get_database():
    if _database is None:
        raise Exception("Database is not connected")
    return _database