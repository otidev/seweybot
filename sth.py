import os
import string

import discord
from dotenv import load_dotenv

load_dotenv("sth.env")
TOKEN = os.getenv("TOKEN")
GUILD_NAME = os.getenv("GUILD_NAME")
intents = discord.Intents.all()

client = discord.Client(intents = intents)

# Actual client code

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == "galen's server":
			break
	print(f"{client.user} has connected to Discord in {guild.name} (id {guild.id})! Press Ctrl-C to exit.")

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	print(message.author)

	if message.content.lower().find("sewey") != -1:
		await message.channel.send("SEWEY!!")
	# We don't swear here-
	if (message.content.lower().find("shit") != -1 or message.content.lower().find("ass") != -1):
		await message.channel.send("BANNING!")
	# Haha moment
	if message.content.lower().find("mora") != -1:
		await message.channel.send("hva sa du om mora mi-")
	if message.content.lower().find("mom") != -1:
		await message.channel.send("watchu say 'bout my mom-")
client.run(TOKEN)