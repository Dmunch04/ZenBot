import asyncio
import ssl

import asyncpg

class Database:
    def __init__ (self, Host, Port, DatabaseName, User, Password):
        self.Host = Host
        self.Port = Port
        self.DatabaseName = DatabaseName
        self.User = User
        self.Password = Password

        self.SSL = ssl.create_default_context (capath='../DB.pem/')
        self.SSL.check_hostname = False
        self.SSL.verify_mode = ssl.CERT_NONE

        Loop = asyncio.get_event_loop ()
        Loop.run_until_complete (self.Setup ())

    async def Setup (self):
        self.Connection = await asyncpg.connect (
            host = self.Host,
            port = self.Port,
            database = self.DatabaseName,
            user = self.User,
            password = self.Password,
            ssl = self.SSL
        )