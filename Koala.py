import discord
import asyncio
import os

# Getting into the good stuff
Koala = discord.Client()

# Symbol that notifies the bot that the message is a command.
commandIdentifier = "$"

@Koala.event
async def on_message(message):
# Checks if the message came from Koala himself, if so, do nothing. :)
    if message.author == Koala.user:
        return ''
    
@Koala.event
async def on_ready():
    print('Connected')
    await Koala.logout()

Koala.run(os.environ['AUTH_TOKEN'])

