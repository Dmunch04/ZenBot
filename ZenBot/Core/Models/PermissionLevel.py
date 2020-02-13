from enum import IntEnum

class PermissionLevel (IntEnum):
    Owner = 5
    Admin = 4
    Moderator = 3
    Supporter = 2
    Default = 1
    Invalid = -1