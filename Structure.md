## ZenBot Code Structure

If you're developing code for ZenBot, please follow this code structure guide. This is ofc. only for the bot. Not the website or anything else. Btw, please add a space between the identifier and arg input start. Example:

Do this:
```py
  def MyFynction (_Arg):
    print (_Arg)

  MyFunction ('Hello, World!')
```

Not:
```py
  def MyFunction(_Arg):
    print(_Arg)

  MyFunction('Hello, World!')
```

<br>

### Strings

We don't use double quotes for strings. Unless we really need to. And try and use F-Strings as much as possible, but if the strings gets long or it needs a lot of input, you can just use format instead.

<br>

### Import Order

First, import packages (Shortest line on top, and longest at bottom)
```py
  import os
  import json
  import shutil
```

Second, import discord packages (Shortest line on top, and longest at bottom)
```py
  import discord
  from discord.ext import commands
```

Third, import scripts in repository (Shortest line on top, and longest at bottom)
```py
  import Config
  from Helpers import EmbedHelper
  from Core import HasPermission, PermissionLevel
```

<br>

### Conventions

#### Function Naming

Use CamelCase for function naming

Example:
```py
  def ExampleFunction ():
    print ('Hello, World!')
```

Not:
```py
  def example_function ():
    print ('Hello, World')
```

#### Function arguments

For normal functions and commands, use underscores before arguments

Example:
```py
  def Example (_Data):
    print (_Data)
```

For init functions, do not user underscores:

```py
  class Example:
    def __init__ (self, Data):
      self.Data = Data
```

<br>

### Local variables passed from context
Create these local variables in commands as needed

```py
  @commands.command()
  async def Example (ctx) {
    Server = ctx.guild
    Channel = ctx.channel
    Sender = ctx.author
    Message = ctx.message
}
```
