import subprocess
import sys
import os

subprocess.call([sys.executable, '-m', 'pip', 'install', 'discord.py'])
subprocess.call([sys.executable, '-m', 'pip', 'install', 'requests'])
subprocess.call([sys.executable, '-m', 'pip', 'install', 'Pillow'])

cwd = os.getcwd()
bat = open("Koala.bat","w+")
bat.write("cd {}\n".format(cwd))
bat.write("py Koala.py")
bat.close()

print("Koala successfully installed. \nPlease run Koala.bat to get started.")
