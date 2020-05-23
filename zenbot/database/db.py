from datetime import datetime

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCursor,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection
)
from typing import (
    Dict,
    Any,
    NoReturn
)


class Database:
    def __init__(self, config: Dict[str, str]):
        self.host = config.get('host', 'localhost') if not config.get('host').strip() == '' else 'localhost'
        self.port = config.get('port', '27017') if not config.get('port').strip() == '' else '27017'
        self.name = config.get('name', 'zenbot') if not config.get('name').strip() == '' else 'zenbot'
        self.username = config.get('username', 'admin') if not config.get('username').strip() == '' else 'admin'
        self.password = config.get('password', 'pwd') if not config.get('password').strip() == '' else 'pwd'
        self.collection = config.get('collection', 'servers') if not config.get('collection').strip() == '' else 'servers'

        self.uri: str = 'mongodb://' + self.username + ':' + self.password + '@' + self.host + ':' + self.port + '/?authSource=' + self.name
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(self.uri)
        self.db: AsyncIOMotorDatabase = self.client.get_database(self.name)
        self.server_collection: AsyncIOMotorCollection = self.db.get_collection(self.collection)

    async def insert(self, document: Dict[str, Any]) -> NoReturn:
        await self.server_collection.insert_one(document)

    async def find_by_id(self, id: str) -> Dict[str, Any]:
        filter: Dict[str, str] = {
            'id': id
        }
        projection: Dict[str, bool] = {
            '_id': False
        }

        cursor: AsyncIOMotorCursor = self.server_collection.find(filter=filter, projection=projection)
        return await cursor.to_list(length=1)

    async def update_by_id(self, id: str, document: Dict[str, Any]) -> NoReturn:
        filter: Dict[str, str] = {
            'id': id
        }
        update = {
            '$set': document,
            '$currentDate': {
                'updatedAt': True
            },
            '$setOnInsert': {
                'createdAt': datetime.utcnow()
            }
        }

        await self.server_collection.update_one(filter, update, upsert=True)

    async def remove_by_id(self, id: str) -> NoReturn:
        filter: Dict[str, str] = {
            'id': id
        }

        await self.server_collection.delete_one(filter)
