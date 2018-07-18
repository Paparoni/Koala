def isGreeting(message):
    if message.content.lower().startswith('hello') or message.content.lower().startswith('hi') or message.content.lower().startswith('hey'):
        return True
    else:
        return False
