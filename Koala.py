import pip
import subprocess
import discord
import asyncio
import KoalaTools as Tools
import git
import re


# Running install as a subprocess as pip.main() is no longer supported. Eliminates the need for requirements.txt
subprocess.check_call(["python", '-m', 'pip', 'install', 'discord.py']);

# Getting into the good stuff
Koala = discord.Client()

# Symbol that notifies the bot that the message is a command.
commandIdentifier = "$"

@Koala.event
async def on_ready():
    print('Logged in')

async def on_message(message):

# Checks if the message came from Koala himself, if so, do nothing. :)
    if message.author == Koala.user:
        return

# Detects if the message is a greeting and just says hello back
    if Tools.isGreeting(message):
        msg_txt = 'Hello {0.author.mention}'.format(message)
        await Koala.send_message(message.channel, msg_txt)


# Start Command Stream
    if message.startswith(commandIdentifier):
        # Get into the nitty gritty

        # Removes the command identifier from the string, easier that way.
        command = Tools.removeStr(message, commandIdentifier)


        # Gets the text after the spaces for the command purpose
        command_index_1 = message.split(' ')[1]
        command_index_2 = message.split(' ')[2]
        command_index_3 = message.split(' ')[3]

        # Now this is where we start writing the commands.
        # Unfortunately this part gets messy because of Python's lack of case/switch
        if command == 'jump':
            msg_txt = 'How High?'
            await Koala.send_message(message.channel, msg_txt)

@Koala.event
async def on_ready():
    print('Connected')
    await Koala.logout()

Koala.run(os.environ['AUTH_TOKEN'])

