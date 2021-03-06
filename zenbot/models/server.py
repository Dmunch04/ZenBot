from datetime import datetime
from typing import Dict, Any, NoReturn

import discord
from discord.ext import commands

from zenbot.utils import spacify_string, Cache
from .member import Member
from .serializable import DBObject


class ServerSettings(DBObject):
    __slots__ = "prefix"

    def __init__(self, prefix=None):
        self.prefix = prefix

    @staticmethod
    def new():
        return ServerSettings(prefix="!")

    def to_dict(self) -> Dict[str, Any]:
        return {"prefix": self.prefix}

    @staticmethod
    def from_dict(data: Dict[str, Any], *args) -> NoReturn:
        self = ServerSettings()
        for key, value in data.items():
            setattr(self, spacify_string(key), value)

        return self


class ServerStats(DBObject):
    __slots__ = ("start_members", "current_members", "messages_sent")

    def __init__(self, start_members=None, current_members=None, messages_sent=None):
        self.start_members = start_members
        self.current_members = current_members
        self.messages_sent = messages_sent

    @staticmethod
    def new(server: discord.Guild):
        return ServerStats(
            start_members=server.member_count,
            current_members=server.member_count,
            messages_sent=0,
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "startMembers": self.start_members,
            "currentMembers": self.current_members,
            "messagesSent": self.messages_sent,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any], *args):
        self = ServerStats()
        for key, value in data.items():
            setattr(self, spacify_string(key), value)

        return self


class Server(DBObject):
    __slots__ = (
        "id",
        "name",
        "owner",
        "members",
        "created_at",
        "settings",
        "stats",
        "joined_at",
        "icon_url",
        "cmd_map",
    )

    def __init__(
        self,
        id=None,
        name=None,
        owner=None,
        members=None,
        created_at=None,
        settings=None,
        stats=None,
        joined_at=None,
        icon_url=None,
        cmd_map=None,
    ):
        self.id = id
        self.name = name
        self.owner = owner
        self.members = members
        self.created_at = created_at
        self.settings = settings
        self.stats = stats
        self.joined_at = joined_at
        self.icon_url = icon_url
        self.cmd_map = cmd_map

        if not isinstance(self.members, Cache) and isinstance(self.members, list):
            self.members = Cache.from_list(self.members, instance=Member, key="id")

    async def update_members_cache(self, server: discord.Guild):
        new_cache = Cache(Member)
        for member in server.members:
            if self.members.has(member.id):
                new_cache.put(member.id, self.members.get(member.id))
            else:
                new_cache.put(member.id, Member.new(member, server))

        self.members = new_cache

    @staticmethod
    def new(bot: commands.Bot, server: discord.Guild):
        return Server(
            id=server.id,
            name=server.name,
            owner=server.owner.id,
            members=[Member.new(member, server) for member in server.members],
            created_at=server.created_at,
            settings=ServerSettings.new(),
            stats=ServerStats.new(server),
            joined_at=server.me.joined_at or datetime.utcnow(),
            icon_url=str(server.icon_url),
            cmd_map=bot.simple_cmd_map,
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": str(self.id),
            "name": str(self.name),
            "owner": str(self.owner),
            "members": [member.to_dict() for member in self.members],
            "createdAt": str(self.created_at),
            "settings": self.settings.to_dict(),
            "stats": self.stats.to_dict(),
            "joinedAt": str(self.joined_at),
            "iconUrl": self.icon_url,
            "cmdMap": self.cmd_map,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any], server: discord.Guild):
        self = Server()
        for key, value in data.items():
            if key in ("id", "owner"):
                value = int(value)
            elif key == "members":
                members = [
                    Member.new(server.get_member(int(member["id"])), server)
                    for member in value
                ]
                value = Cache.from_list(members, instance=Member, key="id")
            elif key == "settings":
                value = ServerSettings.from_dict(value)
            elif key == "stats":
                value = ServerStats.from_dict(value)
            elif key in ("createdAt", "joinedAt"):
                value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")

            setattr(self, spacify_string(key), value)

        return self
