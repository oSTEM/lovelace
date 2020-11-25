# lovelace
oSTEM's custom Discord bot, Lovelace. Happily accepting contributions!

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
- Ensure you have a `.env` file with the token for your test bot (`TOKEN=...`) 
- To run locally, you will need to navigate to the `lovelace` folder and then run the command:
```bash
python -m bot
```