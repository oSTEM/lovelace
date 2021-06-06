import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from constants import COMMAND_PREFIX


class Lovelace(commands.Bot):
    """
    This is the base bot instance.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_extension("exts.affinity_working_groups")

    async def on_ready(self, *args, **kwargs):
        print(f'{bot.user} has connected to Discord')


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    # Intents
    intents = discord.Intents.default()
    intents.members = True


    bot = Lovelace(
        command_prefix=COMMAND_PREFIX,
        activity=discord.Game(name=f"Commands: {COMMAND_PREFIX}help"),
        intents=intents,
        allowed_mentions=discord.AllowedMentions(everyone=False)
    )

    bot.run(TOKEN)