import discord
from discord.ext import commands

from bot.constants import COMMAND_PREFIX


class oSTEMBot(commands.Bot):
    """
    This is the base bot instance.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# Intents
intents = discord.Intents.default()
intents.members = True


bot = oSTEMBot(
    command_prefix=COMMAND_PREFIX,
    activity=discord.Game(name=f"Commands: {COMMAND_PREFIX}help"),
    intents=intents
)


@bot.command(hidden=True)
async def on_ready(self, *args, **kwargs):
    print(f'{bot.user} has connected to Discord')
