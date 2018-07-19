import pip
import subprocess
import discord
import asyncio
import KoalaTools as Tools
import re
import os


# Running install as a subprocess as pip.main() is no longer supported. Eliminates the need for requirements.txt
subprocess.check_call(["python", '-m', 'pip', 'install', 'discord.py']);

# Getting into the good stuff
Koala = discord.Client()

# Symbol that notifies the bot that the message is a command.
commandIdentifier = "$"

async def on_message(message):

# Checks if the message came from Koala himself, if so, do nothing. :)
    if message.author == Koala.user:
        return

# Detects if the message is a greeting and just says hello back
    if Tools.isGreeting(message):
        msg_txt = 'Hello {0.author.mention}'.format(message)
        await Koala.send_message(message.channel, msg_txt

@Koala.event
async def on_ready():
    print('Connected')
    await Koala.logout()

Koala.run(os.environ['AUTH_TOKEN'])

