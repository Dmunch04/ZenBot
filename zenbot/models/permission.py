from enum import IntEnum


class PermissionLevel(IntEnum):
    GUEST = 0
    MEMBER = 1
    MODERATOR = 2
    ADMIN = 3
