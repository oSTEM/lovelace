# lovelace
oSTEM's custom Discord bot, Lovelace. Currently in an alpha state with major rewrites and reorganization to come.

## Set-up Requirements
This is a Python Discord bot that uses the discord.py framework.
- Python 3.6+

Run the command
```bash
python -m pip install -r requirements.txt
```
to install all of the dependencies of this project


## Running the bot on a test server
This bot is tightly coupled with how we set-up our server. 
- The affinity and working groups require that the specific channel names tied to those dictionary constants are present.
- You will need to update the `ACTIVE_GUILD` constant to match the test server. 
