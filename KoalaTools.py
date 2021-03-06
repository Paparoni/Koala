import re
import time

# Detects if the message is a greeting
def isGreeting(message):
    if message.content.lower().startswith('hello') or message.content.lower().startswith('hi') or message.content.lower().startswith('hey'):
        return True
    else:
        return False

# Removes a substring from a string, (really me just testing out my knowledge of Regular Expressions)
def removeStr(str, val):
    regexp = r'[^{0}^[ ]+'.format(val)
    return re.findall(regexp, str)[0];

Drama = [
    '{0} said {1} killed their cat and sold the fur to a homeless man to use as toilet paper.',
    '{0} stole $5000 worth of custom Roblox porn art books from {1}\'s secret drawer :0'
]

def saveTextFile(data, name):
    f = open(name, "w+")
    if type(data) is list:
        for i in data:
            f.write(i+"\n")
    else:
        f.write(data)
    f.close()

def updateTextFile(data, name):
    f = open(name, "a+")
    f.write(data)
    f.close()

def saveMessageLog(messages):
    date = time.strftime("%m-%d-%y", time.localtime())
    saveTextFile(messages, date+"_messagelog.txt")
