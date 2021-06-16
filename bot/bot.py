import os

import discord
from dislash import SlashClient
from discord.ext import commands

from constants import COMMAND_PREFIX, LOG_CHANNEL


class Lovelace(commands.Bot):
    """
    This is the base bot instance.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_extension("exts.affinity_working_groups")

    async def on_ready(self, *args, **kwargs):
        await self.get_channel(LOG_CHANNEL).send("I have connected.")


if __name__ == "__main__":
    TOKEN = os.getenv('TOKEN')

    # Intents
    intents = discord.Intents.default()
    intents.members = True


    bot = Lovelace(
        command_prefix=COMMAND_PREFIX,
        acitivty=None,
        intents=intents,
        allowed_mentions=discord.AllowedMentions(everyone=False)
    )

    slash = SlashClient(bot)

    bot.run(TOKEN)