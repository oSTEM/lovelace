# Lovelace
oSTEM's custom Discord bot, Lovelace. Happily accepting contributions!

This bot uses the discord.py library for the basic bot functionality and uses dislash.py for Slash Commands support.

The main purpose of the bot is to provide functionality for joining Affinity and Working groups securely 

# Set-up Requirements
This is a Python Discord bot that uses the discord.py and dislash.py frameworks.
It requires python 3.6+ but it currently using what is specified in the `Dockerfile`.

Additional, this bot uses Docker to run the application.
The commands to build the docker image and to run the container are as follows:

```bash
docker build -t lovelace .
```

```bash
docker run -e "TOKEN=token_goes_here" lovelace
```

The `register_command.py` file is required to run once and requires an adjustment to the `Dockerfile`, specifically the file for `CMD`. This registers the Slash Commands for the specified Guild.

Once the commands are registered for the guild, the bot can be re-run normally with the Docker commands listed above.
