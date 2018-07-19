import re

# Detects if the message is a greeting
def isGreeting(message):
    if message.content.lower().startswith('hello') or message.content.lower().startswith('hi') or message.content.lower().startswith('hey'):
        return True
    else:
        return False

# Removes a substring from a string, (really me just testing out my knowledge of Regular Expressions)
def removeStr(str, val):
    regexp = r'[^{0}]+'.format(val)
    return re.findall(regexp, str);
