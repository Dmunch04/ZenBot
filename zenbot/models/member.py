import calendar
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta, MO

import discord

from typing import Dict, Any, Optional

from zenbot.utils import spacify_string
from .permission import PermissionLevel
from .serializable import DBObject


class Mute(object):
    __slots__ = (
        "duration",
        "moderator",
        "reason",
        "timestamp",
        "expires_at",
        "is_expired",
    )

    def __init__(
        self,
        duration,
        moderator,
        reason="Unreasoned",
        timestamp=datetime.utcnow(),
        expires_at=None,
        is_expired=False,
    ):
        self.duration = duration
        self.moderator = moderator
        self.reason = reason
        self.timestamp = timestamp
        self.expires_at = expires_at or self._calculate_expires_at(duration, timestamp)
        # TODO: it actually executes the latter if `is_expired` is false right? eh
        self.is_expired = is_expired or (self.timestamp <= self.expires_at)

    def _calculate_expires_at(
        self, duration: str, timestamp: datetime
    ) -> Optional[datetime]:
        import re

        match = re.match(r"(\d+)([smhdwMy])", duration)
        if match:
            if match.group(2) == "s":
                return timestamp + timedelta(seconds=int(match.group(1)))
            elif match.group(2) == "m":
                return timestamp + timedelta(minutes=int(match.group(1)))
            elif match.group(2) == "h":
                return timestamp + timedelta(hours=int(match.group(1)))
            elif match.group(2) == "d":
                return timestamp + timedelta(days=int(match.group(1)))
            elif match.group(2) == "w":
                return timestamp + timedelta(weeks=int(match.group(1)))
            elif match.group(2) == "M":
                return timestamp + relativedelta(months=int(match.group(1)))
            elif match.group(2) == "y":
                return timestamp + relativedelta(years=int(match.group(1)))

        return None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "duration": self.duration,
            "moderator": str(self.moderator),
            "reason": self.reason,
            "timestamp": str(self.timestamp),
            "expiresAt": str(self.expires_at),
            "isExpired": self.is_expired,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        return Mute(
            data.get("duration"),
            int(data.get("moderator")),
            data.get("reason"),
            datetime.strptime(data.get("timestamp"), "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime(data.get("expiresAt"), "%Y-%m-%d %H:%M:%S.%f"),
            data.get("isExpired"),
        )


class Warn(object):
    __slots__ = ("reason", "moderator", "timestamp")

    def __init__(self, reason, moderator, timestamp=datetime.utcnow()):
        self.reason = reason
        self.moderator = moderator
        self.timestamp = timestamp

    def to_dict(self) -> Dict[str, Any]:
        return {
            "reason": self.reason,
            "moderator": str(self.moderator),
            "timestamp": str(self.timestamp),
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        return Warn(
            data.get("reason"),
            int(data.get("moderator")),
            datetime.strptime(data.get("timestamp"), "%Y-%m-%d %H:%M:%S.%f"),
        )


class Member(DBObject):
    __slots__ = (
        "id",
        "name",
        "muted",
        "perm_level",
        "perms",
        "messages_sent",
        "mutes",
        "warns",
    )

    def __init__(
        self,
        id=None,
        name=None,
        muted=None,
        perm_level=None,
        perms=None,
        messages_sent=None,
        mutes=None,
        warns=None,
    ):
        self.id = id
        self.name = name
        self.muted = muted
        self.perm_level = perm_level
        self.perms = perms
        self.messages_sent = messages_sent
        self.mutes = mutes
        self.warns = warns

    @staticmethod
    def new(member: discord.Member, server: discord.Guild):
        return Member(
            id=member.id,
            name=member.name,
            muted=False,
            perm_level=PermissionLevel.GUEST,
            perms=[],
            messages_sent=0,
            mutes=[],
            warns=[],
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": str(self.id),
            "name": str(self.name),
            "muted": self.muted,
            "permLevel": self.perm_level.value,
            "perms": self.perms,
            "messagesSent": self.messages_sent,
            "mutes": [mute.to_dict() for mute in self.mutes],
            "warns": [warn.to_dict() for warn in self.warns],
        }

    @staticmethod
    def from_dict(data: Dict[str, Any], *args):
        self = Member()
        for key, value in data.items():
            if key in ("id", "serverId"):
                value = int(value)
            elif key == "permLevel":
                value = PermissionLevel(value)
            elif key == "mutes":
                value = [Mute.from_dict(mute) for mute in value]
            elif key == "warns":
                value = [Warn.from_dict(warn) for warn in value]

            setattr(self, spacify_string(key), value)

        return self
