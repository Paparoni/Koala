import discord
import random
import KoalaTools as Tools
import requests
import json
from PIL import Image
import urllib.request
import shutil
import os
import socket

Koala = discord.Client()
commandIdentifier = "$"
@Koala.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == Koala.user:
        return

        # Detects if the message is a greeting and just says hello back
    if Tools.isGreeting(message):
        msg_txt = 'Hello {0.author.mention}'.format(message)
        await Koala.send_message(message.channel, msg_txt)


    # Start Command Stream
    if message.content.startswith(commandIdentifier):
        # Get into the nitty gritty

        # Removes the command identifier from the string, easier that way.
        command = Tools.removeStr(message.content, commandIdentifier)
        # Gets the name of the person that used the command
        commandUser = message.author

        # Gets the text after the spaces for the command purpose
        if len(message.content.split(' ')) == 2:
            command_index_1 = message.content.split(' ')[1] or ''
        elif len(message.content.split(' ')) == 3:
            command_index_2 = message.content.split(' ')[2] or ''
        elif len(message.content.split(' ')) == 4:
            command_index_3 = message.content.split(' ')[3] or ''
        else:
            ''
        # Now this is where we start writing the commands.
        # Unfortunately this part gets messy because of Python's lack of case/switch
        if command == 'jump':
            members = list(Koala.get_all_members())
            msg_txt = 'How High? {}'.format(commandUser.mention)
            await Koala.send_message(message.channel, msg_txt)
        elif command == 'logout':
            await Koala.logout()

        elif command == 'drama':
            # Make a list out of the get_all_members() generator
            members = list(Koala.get_all_members())
            # Randomly grab one person from the member list
            person1 = random.choice(members)
            person2 = random.choice(members)

            # Randomly grab one situation from the drama list
            situation = random.choice(Tools.Drama);

            msg_txt = situation.format(person1.mention, person2.mention)
            await Koala.send_message(message.channel, msg_txt)

        elif command == 'define':
            # URL to urban dictionary api
            UD_URL = 'http://api.urbandictionary.com/v0/define?term='
            word = command_index_1
            # Request JSON data on the word from Urban Dictionary API
            wordREQ = requests.get(UD_URL+word)
            # Convert data to JSON
            wordData = wordREQ.json()
            definition = wordData['list'][0]['definition']
            example = wordData['list'][0]['example']

            fin_txt = '{}'.format(definition)
            ex_text = 'Example: {}'.format(example)

            await Koala.send_message(message.channel, fin_txt)
            await Koala.send_message(message.channel, ex_text)

        elif command == 'bigdick':
            # Draws user avatar over big dick man  ( ͡° ͜ʖ ͡°)

            # Request the user profile image from discord and send with a Mozilla header or else you'll get a 403 Forbidden error
            r = requests.get("https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png".format(commandUser), headers={'User-Agent': 'Mozilla/5.0'}, stream=True)
            if r.status_code == 200:
                # Download the raw image and copy it to a file
                with open('Images/in.png', 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
            background = Image.open('Images/bd.jpg', 'r')
            img = Image.open('Images/in.png', 'r')
            offset = 180,15
            background.paste(img, offset)
            background.save('Images/out.png')
            await Koala.send_file(message.channel, 'Images/out.png')
@Koala.event
async def on_ready():
    print('Connected')



Koala.run(os.environ['AUTH_TOKEN'])
