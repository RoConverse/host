import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord import Game
import os

token = os.getenv("token")
email = os.getenv("email")
password = os.getenv("password")
Client = discord.client
client = commands.Bot(command_prefix = '3182309139')
Clientdiscord = discord.Client()

client.run(email, password, bot=False)
