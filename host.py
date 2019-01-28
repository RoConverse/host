from discord.ext import commands
import os
client=commands.Bot("sdadasjkdaksjnadk")
@client.event
async def on_ready():
  await client.change_presence(game=discord.Game(name="with kermit"))
client.run(os.getenv("token"), bot=False)
