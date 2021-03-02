from .serializable import DBObject

from discord import Guild
from datetime import datetime

from typing import (
    Dict,
    Any
)


class ServerSettings(DBObject):
    __slots__ = (
        'prefix'
    )

    def __init__(self, prefix: str = '!'):
        self.prefix = prefix

    @property
    def prefix(self) -> str:
        return self.prefix

    @prefix.setter
    def prefix(self, s: str):
        self.prefix = s

    def to_dict(self) -> Dict[str, Any]:
        return {
            'prefix': self.prefix
        }


class ServerStats(DBObject):
    __slots__ = (
        'start_members', 'current_members'
    )

    def __init__(self, start_members: int = 0, current_members: int = 0):
        self.start_members = start_members
        self.current_members = current_members

    def to_dict(self) -> Dict[str, Any]:
        return {
            'startsMembers': self.start_members,
            'currentMembers': self.current_members
        }


# TODO: Members?
class Server(DBObject):
    __slots__ = (
        'id', 'name', 'owner',
        'region', 'settings', 'stats',
        'joined_at'
    )

    def __init__(self, server: Guild):
        self.id = server.id
        self.name = server.name
        self.owner = server.owner_id
        self.region = server.region
        self.settings = ServerSettings()
        self.stats = ServerStats()
        self.joined_at = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'owner': self.owner,
            'region': self.region,
            'settings': self.settings,
            'stats': self.stats,
            'joinedAt': self.joined_at
        }
