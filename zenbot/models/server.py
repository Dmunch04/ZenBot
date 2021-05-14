from .serializable import DBObject
from .permission import PermissionLevel
from zenbot.utils import spacify_string

import discord
from datetime import datetime

from typing import Dict, Any, NoReturn


# TODO: im not sure the way the whole model system works with loading and writing from/to the db
#  but well it works for now. it might not be very scalable or good,
#  so make sure to keep looking for better solutions to this system


class ServerSettings(DBObject):
    __slots__ = "prefix"

    @staticmethod
    def new():
        self = ServerSettings()

        self.prefix = "!"

        return self

    def to_dict(self) -> Dict[str, Any]:
        return {"prefix": self.prefix}

    def from_dict(self, data: Dict[str, Any]) -> NoReturn:
        for key, value in data.items():
            setattr(self, spacify_string(key), value)


class ServerStats(DBObject):
    __slots__ = ("start_members", "current_members", "messages_sent")

    @staticmethod
    def new(server: discord.Guild):
        self = ServerStats()

        self.start_members = server.member_count
        self.current_members = self.start_members
        self.messages_sent = 0

        return self

    def to_dict(self) -> Dict[str, Any]:
        return {
            "startMembers": self.start_members,
            "currentMembers": self.current_members,
            "messagesSent": self.messages_sent,
        }

    def from_dict(self, data: Dict[str, Any]) -> NoReturn:
        for key, value in data.items():
            setattr(self, spacify_string(key), value)


class Member(DBObject):
    __slots__ = (
        "server_instance",
        "member_instance",
        "id",
        "server_id",
        "name",
        "muted",
        "perm_level",
        "perms",
        "messages_sent",
    )

    def __init__(self, member: discord.Member, server: discord.Guild):
        self.server_instance = server
        self.member_instance = member

    def new(self) -> NoReturn:
        self.id = self.member_instance.id
        self.server_id = self.server_instance.id
        self.name = self.member_instance.name
        self.muted = False
        self.perm_level = PermissionLevel.GUEST
        self.perms = []
        self.messages_sent = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": str(self.id),
            "serverId": str(self.server_id),
            "name": str(self.name),
            "muted": self.muted,
            "permLevel": self.perm_level.value,
            "perms": self.perms,
            "messagesSent": self.messages_sent,
        }

    def from_dict(self, data: Dict[str, Any]) -> NoReturn:
        for key, value in data.items():
            if key in ("id", "serverId"):
                value = int(value)
            elif key == "permLevel":
                value = PermissionLevel(value)

            setattr(self, spacify_string(key), value)


class Server(DBObject):
    __slots__ = (
        "server_instance",
        "id",
        "name",
        "owner",
        "members",
        "created_at",
        "settings",
        "stats",
        "joined_at",
        "icon_url",
    )

    def __init__(self, server: discord.Guild):
        self.server_instance = server

    def new(self) -> NoReturn:
        self.id = self.server_instance.id
        self.name = self.server_instance.name
        self.owner = self.server_instance.owner_id
        self.members = [
            Member(member, self.server_instance)
            for member in self.server_instance.members
        ]
        [member.new() for member in self.members]
        self.created_at = self.server_instance.created_at
        self.settings = ServerSettings.new()
        self.stats = ServerStats.new(self.server_instance)
        self.joined_at = self.server_instance.me.joined_at or datetime.utcnow()
        self.icon_url = str(self.server_instance.icon_url)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": str(self.id),
            "name": str(self.name),
            "owner": str(self.owner),
            "members": [member.to_dict() for member in self.members],
            "settings": self.settings.to_dict(),
            "stats": self.stats.to_dict(),
            "joinedAt": str(self.joined_at),
            "iconUrl": self.icon_url,
        }

    def from_dict(self, data: Dict[str, Any]) -> NoReturn:
        for key, value in data.items():
            if key in ("id", "owner"):
                value = int(value)
            elif key == "members":
                members = []
                for member in value:
                    member_instance = Member(
                        self.server_instance.get_member(int(member["id"])),
                        self.server_instance,
                    )
                    member_instance.from_dict(member)
                    members.append(member_instance)
                value = members
            elif key == "settings":
                settings = ServerSettings()
                settings.from_dict(value)
                value = settings
            elif key == "stats":
                stats = ServerStats()
                stats.from_dict(value)
                value = stats
            elif key == "joinedAt":
                value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")

            setattr(self, spacify_string(key), value)


class DBTestObject:
    __slots__ = ("some_obj", "a", "b", "c")

    def __init__(self, some_obj):
        self.some_obj = some_obj
        self.a = getattr(some_obj, "a", 0)
        self.b = getattr(some_obj, "a", 1)
        self.c = getattr(some_obj, "a", 2)

    @staticmethod
    def new():
        return DBTestObject.from_dict(
            {
                "a": 0,
                "b": 1,
                "c": 2,
            }
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "a": self.a,
            "b": self.b,
            "c": self.c,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        self = DBTestObject(None)  # ?
        for key, value in data.items():
            setattr(self, key, value)

        return self


# isnt this basically like the current method? or at least very close tbh
class OtherDBTestObject:
    __slots__ = ("test_obj", "a", "b", "c")

    # create empty? (this shouldnt be used then perhaps?)
    def __init__(self, a=2, b=1, c=0):
        self.a = a
        self.b = b
        self.c = c

    # create empty using the test_obj values and also setting the test_obj in the process
    @staticmethod
    def new(test_obj: DBTestObject):
        self = OtherDBTestObject(
            a=test_obj.a,
            b=test_obj.b,
            c=str(test_obj.c),
        )
        self.test_obj = test_obj

        return self

    # make it into a dict
    def to_dict(self) -> Dict[str, Any]:
        return {
            "a": self.a,
            "b": self.b,
            "c": self.c,
        }

    # load it from a dict
    @staticmethod
    def from_dict(data: Dict[str, Any]):
        self = OtherDBTestObject()
        for key, value in data.items():
            if key == "c":
                value = str(value)

            setattr(self, key, value)

        return self


class ImprovedDBObject:
    __slots__ = ("a", "b", "c")

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def new(obj: DBTestObject):
        return ImprovedDBObject(
            a=obj.a,
            b=obj.b,
            c=obj.c,
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "a": self.a,
            "b": self.b,
            "c": self.c,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        self = ImprovedDBObject()
        for key, value in data.items():
            setattr(self, key, value)

        return self
