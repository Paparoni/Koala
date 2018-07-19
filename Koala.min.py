import discord #line:1
import random #line:2
import KoalaTools as Tools #line:3
import requests #line:4
import json #line:5
from PIL import Image #line:6
import urllib .request #line:7
import shutil #line:8
import os #line:9
import socket #line:10
HOST =''#line:12
PORT =os .environ ['PORT']#line:13
s =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:14
s .bind ((HOST ,PORT ))#line:15
s .listen (1 )#line:16
Koala =discord .Client ()#line:19
commandIdentifier ="$"#line:20
@Koala .event #line:21
async def on_message (O0O000O000OOO0OO0 ):#line:22
    if O0O000O000OOO0OO0 .author ==Koala .user :#line:24
        return #line:25
    if Tools .isGreeting (O0O000O000OOO0OO0 ):#line:28
        O0OO000OO00O000O0 ='Hello {0.author.mention}'.format (O0O000O000OOO0OO0 )#line:29
        await Koala .send_message (O0O000O000OOO0OO0 .channel ,O0OO000OO00O000O0 )#line:30
    if O0O000O000OOO0OO0 .content .startswith (commandIdentifier ):#line:34
        O00O0000OO00O0000 =Tools .removeStr (O0O000O000OOO0OO0 .content ,commandIdentifier )#line:38
        OOO0OOOO00O00O00O =O0O000O000OOO0OO0 .author #line:40
        if len (O0O000O000OOO0OO0 .content .split (' '))==2 :#line:43
            OOO00O000O00OOOO0 =O0O000O000OOO0OO0 .content .split (' ')[1 ]or ''#line:44
        elif len (O0O000O000OOO0OO0 .content .split (' '))==3 :#line:45
            OO00O00O0OO0OOOO0 =O0O000O000OOO0OO0 .content .split (' ')[2 ]or ''#line:46
        elif len (O0O000O000OOO0OO0 .content .split (' '))==4 :#line:47
            OO00OOOO00O000O0O =O0O000O000OOO0OO0 .content .split (' ')[3 ]or ''#line:48
        else :#line:49
            ''#line:50
        if O00O0000OO00O0000 =='jump':#line:53
            O0O000OOOOOOO0000 =list (Koala .get_all_members ())#line:54
            O0OO000OO00O000O0 ='How High? {}'.format (OOO0OOOO00O00O00O .mention )#line:55
            await Koala .send_message (O0O000O000OOO0OO0 .channel ,O0OO000OO00O000O0 )#line:56
        elif O00O0000OO00O0000 =='logout':#line:57
            await Koala .logout ()#line:58
        elif O00O0000OO00O0000 =='drama':#line:60
            O0O000OOOOOOO0000 =list (Koala .get_all_members ())#line:62
            O0O000000O0O000OO =random .choice (O0O000OOOOOOO0000 )#line:64
            OOOOOO00OOOOOO0O0 =random .choice (O0O000OOOOOOO0000 )#line:65
            O000OO00OO00O00OO =random .choice (Tools .Drama );#line:68
            O0OO000OO00O000O0 =O000OO00OO00O00OO .format (O0O000000O0O000OO .mention ,OOOOOO00OOOOOO0O0 .mention )#line:70
            await Koala .send_message (O0O000O000OOO0OO0 .channel ,O0OO000OO00O000O0 )#line:71
        elif O00O0000OO00O0000 =='define':#line:73
            OO0OO00O0O0O0OO00 ='http://api.urbandictionary.com/v0/define?term='#line:75
            O000O00OO0O0O00OO =OOO00O000O00OOOO0 #line:76
            O0000O0000OO00O00 =requests .get (OO0OO00O0O0O0OO00 +O000O00OO0O0O00OO )#line:78
            OO0O000OOO0OO000O =O0000O0000OO00O00 .json ()#line:80
            O00O0O000O0O0000O =OO0O000OOO0OO000O ['list'][0 ]['definition']#line:81
            O0000O0OOO0OOO0O0 =OO0O000OOO0OO000O ['list'][0 ]['example']#line:82
            OO000000OOO00OO0O ='{}'.format (O00O0O000O0O0000O )#line:84
            OO0O00OOOOOO0O000 ='Example: {}'.format (O0000O0OOO0OOO0O0 )#line:85
            await Koala .send_message (O0O000O000OOO0OO0 .channel ,OO000000OOO00OO0O )#line:87
            await Koala .send_message (O0O000O000OOO0OO0 .channel ,OO0O00OOOOOO0O000 )#line:88
        elif O00O0000OO00O0000 =='bigdick':#line:90
            O000O000O0OO0O0OO =requests .get ("https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png".format (OOO0OOOO00O00O00O ),headers ={'User-Agent':'Mozilla/5.0'},stream =True )#line:94
            if O000O000O0OO0O0OO .status_code ==200 :#line:95
                with open ('Images/in.png','wb')as OOOOO00OO00000OO0 :#line:97
                    O000O000O0OO0O0OO .raw .decode_content =True #line:98
                    shutil .copyfileobj (O000O000O0OO0O0OO .raw ,OOOOO00OO00000OO0 )#line:99
            O0000000OO00OOOO0 =Image .open ('Images/bd.jpg','r')#line:100
            O0000O00O0OO0OO0O =Image .open ('Images/in.png','r')#line:101
            O00O00OOO0OO0OOOO =180 ,15 #line:102
            O0000000OO00OOOO0 .paste (O0000O00O0OO0OO0O ,O00O00OOO0OO0OOOO )#line:103
            O0000000OO00OOOO0 .save ('Images/out.png')#line:104
            await Koala .send_file (O0O000O000OOO0OO0 .channel ,'Images/out.png')#line:105
@Koala .event #line:106
async def on_ready ():#line:107
    print ('Connected')#line:108
Koala .run (os .environ ['AUTH_TOKEN'])
