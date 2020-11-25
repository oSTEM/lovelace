import discord
from discord.ext import commands

from bot.bot import bot
from bot.constants import ACTIVE_GUILD, AFFINITY_GROUPS, WORKING_GROUPS
from bot.utils.role_checks import _has_role_check


class WorkingGroups(commands.Cog):
    """A cog that manages users adding themslves and leaving Working Groups"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def join_wg(self, ctx: commands.Context, *, working_group: str) -> None:
        """Direct Message the bot with the affinity group they want to join. The bot will add you to the correct group.

        The current working groups can be found on the oSTEM.org website.
        """
        guild = discord.utils.get(bot.guilds, name=ACTIVE_GUILD)
        if await _has_role_check(ctx, guild, "Member"):
            category = discord.utils.get(guild.categories, name="Working Groups")
            await _add_remove_from_group(ctx, working_group, category, True)
        else:
            msg_content = """Sorry, you have not accepted the server rules yet.\
                           \nPlease read the #welcome channel and click on the existing reaction emoji to agree to the server rules."""
            await ctx.author.send(msg_content)

    @commands.command()
    async def leave_wg(self, ctx: commands.Context, *, working_group: str) -> None:
        """Direct Message the bot with the affinity group that you would like to leave.
        The bot will remove you from the group."""
        guild = discord.utils.get(bot.guilds, name=ACTIVE_GUILD)
        category = discord.utils.get(guild.categories, name="Working Groups")
        await _add_remove_from_group(ctx, working_group, category, False)


class AffinityGroups(commands.Cog):
    """A cog that manages users adding themselves and leaving Affinity Groups"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def join_ag(self, ctx: commands.Context, *, affinity_group: str) -> None:
        """Direct Message the bot with the affinity group they want to join. The bot will add you to the correct group.

        The current affinity groups can be found on the oSTEM.org website
        """
        guild = discord.utils.get(bot.guilds, name=ACTIVE_GUILD)
        if await _has_role_check(ctx, guild, "Member"):
            category = discord.utils.get(guild.categories, name="affinity groups")
            await _add_remove_from_group(ctx, affinity_group, category, True)
        else:
            msg_content = """Sorry, you have not accepted the server rules yet.\
                           \nPlease read the #welcome channel and click on the existing reaction emoji to agree to the server rules."""
            await ctx.author.send(msg_content)

    @commands.command()
    async def leave_ag(self, ctx: commands.Context, *, affinity_group: str) -> None:
        """Direct Message the bot with the affinity group that you would like to leave.
        The bot will remove you from the group."""

        guild = discord.utils.get(bot.guilds, name=ACTIVE_GUILD)
        category = discord.utils.get(guild.categories, name="affinity groups")
        await _add_remove_from_group(ctx, affinity_group, category, False)


async def _add_remove_from_group(ctx: commands.Context, channel_name: str, category,  add: bool = True) -> bool:
    """Helper function to add or remove a user from a specific channel.
    If add is false, it will remove the permissions."""

    guild = discord.utils.get(bot.guilds, name=ACTIVE_GUILD)

    active_group = ''
    if category.name == "affinity groups":
        active_group = AFFINITY_GROUPS
    elif category.name == "Working Groups":
        active_group = WORKING_GROUPS

    msg_content = ":x: Sorry, there was an error. Please try again or contact an admin."

    for key, value in active_group.items():
        if channel_name.lower() in value:
            channel = discord.utils.get(guild.channels, category_id=category.id, name=key)
            await channel.set_permissions(ctx.author, read_messages=add, send_messages=add, add_reactions=add,
                                          read_message_history=add, external_emojis=add, attach_files=add,
                                          embed_links=add)
            if add is True:
                result = "added"
            else:
                result = "removed"
            msg_content = f":white_check_mark: You have been successfully {result} from the {key} affinity group channel.\
                \nIf there was an error, please contact an admin."
    await ctx.author.send(msg_content)
    if ctx.channel.type is discord.ChannelType.text:
        # If the message was in a public channel, we will delete the message to maintain privacy
        await ctx.message.delete()


def setup(bot: commands.Bot) -> None:
    """Load Affinity and Working Groups cogs"""
    bot.add_cog(AffinityGroups(bot))
    bot.add_cog(WorkingGroups(bot))
