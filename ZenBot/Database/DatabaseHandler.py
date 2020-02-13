import asyncio
import asyncpg

class Database:
    def __init__ (self, Host, Port, DatabaseName, User, Password):
        self.Host = Host
        self.Port = Port
        self.DatabaseName = DatabaseName
        self.User = User
        self.Password = Password

        """
        self.ConnectionPool = await asyncpg.connect (
            host = Host,
            port = Port,
            database = DatabaseName,
            user = User,
            password = Password,
        )
        """