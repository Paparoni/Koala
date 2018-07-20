import discord
import random
import KoalaTools as Tools
import requests
import json
from PIL import Image
import urllib.request
import shutil
import os



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
        print(message.content.split(' '))
        if len(message.content.split(' ')) == 2:
            command_index_1 = message.content.split(' ')[1]
        elif len(message.content.split(' ')) == 3:
            command_index_1 = message.content.split(' ')[1]
            command_index_2 = message.content.split(' ')[2]
        elif len(message.content.split(' ')) == 4:
            command_index_1 = message.content.split(' ')[1]
            command_index_2 = message.content.split(' ')[2]
            command_index_3 = message.content.split(' ')[3]
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

            # command that uses the fortnite tracker API to retrieve stats
        elif command == 'fortnite':
            user = command_index_1
            platform = command_index_2
            if platform.lower() == 'ps4' or platform.lower() == 'ps' or platform.lower() == 'playstation':
                platform = 'psn'
            elif platform.lower() == 'xbox' or platform.lower() == 'xbox1' or platform.lower() == 'xboxone' or platform.lower() == 'xb1':
                platform = 'xb1'
            elif platform.lower() == 'pc':
                platform = 'pc'
            else:
                'do some error handling'

            TRN_URL = 'https://api.fortnitetracker.com/v1/profile/{1}/{0}'.format(user, platform)
            print(TRN_URL)
            fn_data = requests.get(TRN_URL, headers={'TRN-Api-Key': os.environ['TRN-Api-Key']})
            print(fn_data.text)
            fn = fn_data.json()['lifeTimeStats']
            epicUserHandle = fn_data.json()['epicUserHandle']
            KD = fn[11]['value']
            matches = fn[7]['value']
            kills = fn[10]['value']
            wins = fn[8]['value']
            top5 = fn[0]['value']
            top10 = fn[3]['value']

            stat_line = 'Lifetime Fortnite stats for {1}: \nMatches: {2} \nKills: {3} \nK/D Ratio: {0} \nWins: {4} Top 5: {5} Top 10: {6}'.format(KD, epicUserHandle, matches, kills, wins, top5, top10)
            await Koala.send_message(message.channel, stat_line)

@Koala.event
async def on_ready():
    print('Connected')


Koala.run(os.environ['AUTH_TOKEN'])
