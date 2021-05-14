from enum import IntEnum


class PermissionLevel(IntEnum):
    INVALID = -1
    GUEST = 0
    MEMBER = 1
    MODERATOR = 2
    ADMIN = 3
    OWNER = 4
