import os

import discord
from dislash import SlashClient, Option, Type, SlashCommand, OptionChoice
from discord.ext import commands
from dislash.slash_commands import slash_client

from constants import COMMAND_PREFIX, GUILD_ID


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
    TOKEN = os.getenv('TOKEN')

    # Intents
    intents = discord.Intents.default()
    intents.members = True


    bot = Lovelace(
        command_prefix=COMMAND_PREFIX,
        intents=intents,
        allowed_mentions=discord.AllowedMentions(everyone=False)
    )

    slash = SlashClient(bot)


    @slash.event
    async def on_ready():
        sc = SlashCommand(name="working-group",
            description="Join or leave a working group",
            options=[
                Option(name="join", description="Join a working group", type=Type.STRING,
                    choices=[
                        OptionChoice(name="Beyond the Binary", value="beyondthebinary"),
                        OptionChoice(name="Black & Queer", value="black_queer"),
                        OptionChoice(name="Queer Enabled", value="queer-enabled"),
                    ]
                ),
                Option(name="leave", description="Leave a working group", type=Type.STRING,
                    choices=[
                        OptionChoice(name="Beyond the Binary", value="beyondthebinary"),
                        OptionChoice(name="Black & Queer", value="black_queer"),
                        OptionChoice(name="Queer Enabled", value="queer-enabled"),
                    ]
                )
            ]
        )
        
        sc1 = SlashCommand(name="affinity-group",
            description="Join or leave an affinity group",
            options=[
                Option(name="join", description="Join an affinity group", type=Type.STRING,
                    choices=[
                        OptionChoice(name="AAPI", value="aapi"),
                        OptionChoice(name="Ace/Aro", value="acearo"),
                        OptionChoice(name="(Dis)Ability", value="disability"),
                        OptionChoice(name="InQueery", value="inqueery"),
                        OptionChoice(name="Middle Sexualities", value="middle-sexualities"),
                        OptionChoice(name="Race and Ethnicity", value="race-ethnicity"),
                        OptionChoice(name="Trans and Non-binary", value="transnon-binary"),
                        OptionChoice(name="Women", value="women")

                    ]
                ),
                Option(name="leave", description="Leave an affinity group", type=Type.STRING,
                    choices=[
                        OptionChoice(name="AAPI", value="aapi"),
                        OptionChoice(name="Ace/Aro", value="acearo"),
                        OptionChoice(name="(Dis)Ability", value="disability"),
                        OptionChoice(name="InQueery", value="inqueery"),
                        OptionChoice(name="Middle Sexualities", value="middle-sexualities"),
                        OptionChoice(name="Race and Ethnicity", value="race-ethnicity"),
                        OptionChoice(name="Trans and Non-binary", value="transnon-binary"),
                        OptionChoice(name="Women", value="women")

                    ]
                )
            ]
        )

        await slash.register_guild_slash_command(GUILD_ID, sc)
        await slash.register_guild_slash_command(GUILD_ID, sc1)


    bot.run(TOKEN)
