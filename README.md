# Koala
A better, more family friendly Discord bot created in Python

# Setup (Windows)
## Note due to async now being a reserved word Discord.py only works in Python 3.6
### Setting the auth token as an environment variable
### Open Windows PowerShell
### Run Line
`[Environment]::SetEnvironmentVariable("AUTH_TOKEN", Put Your Auth Token Here, "User")`
### Alternatively you could just replace os.environ["AUTH_TOKEN"] with your actual auth token, but I wouldn't recommend this in case you want to share the code.

### For local hosting Run
	`py Installer.py`
	
### After running Installer.py the bot can be started by opening Koala.bat
