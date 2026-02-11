import discord
from dotenv import load_dotenv
import os

load_dotenv() # loads .env file

# get the following variables from .env file
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN") # this is sensitive information and is the main reason .env file is used, plus it makes everything neater
STEAM_USER_ID = int(os.getenv("STEAM_USER_ID")) # convert to int for comparison with message.author.id
EPIC_USER_ID = int(os.getenv("EPIC_USER_ID"))
PING_ROLE_ID = os.getenv("PING_ROLE_ID")  # keep as string for mention formatting

# main class for the bot, inherits from discord.Client
class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user: # ignore own messages, else we could have an infinite loop of the bot responding to itself
            return

        # comparison and pinging logic
        if message.author.id == STEAM_USER_ID:
            await message.channel.send(f'<@&{PING_ROLE_ID}> game from steam.')
        
        elif message.author.id == EPIC_USER_ID:
            await message.channel.send(f'<@&{PING_ROLE_ID}> from epic games.')

# set up the bot with the necessary intents and run it
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(DISCORD_BOT_TOKEN)