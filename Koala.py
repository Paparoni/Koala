import pip
import subprocess
import discord
import asyncio
import KoalaTools as Tools
import git


# Running install as a subprocess as pip.main() is no longer supported
subprocess.check_call(["python", '-m', 'pip', 'install', 'discord.py']);
subprocess.check_call(["python", '-m', 'pip', 'install', 'GitPython']);

# Getting into the good stuff
Koala = discord.Client()

@Koala.event
async def on_ready():
    print('Logged in')

async def on_message(message):
    if message.author == Koala.user:
        return

    if (Tools.isGreeting(message)):
        msg_txt = 'Hello {0.author.mention}'.format(message)
        await Koala.send_message(message.channel, msg_txt)

@Koala.event
async def on_ready():
    print('Connected')
    await Koala.logout()

Koala.run('')

