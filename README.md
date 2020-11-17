# lovelace
oSTEM's custom Discord bot, Lovelace. Currently in an alpha state with major rewrites and reorganization to come.

## Set-up Requirements
This is a Python Discord bot that uses the discord.py framework.
- Python 3.6+
- `python -m pip install discord`
- `python -m pip install dotenv`


## Running the bot on a test server
This bot is tightly coupled with how we set-up our server. 
- The affinity and working groups require that the specific channel names tied to those dictionary constants are present.
- You will need to update the `ACTIVE_GUILD` constant to match the test server. 
