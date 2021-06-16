import discord
from discord.ext import commands
from dislash import slash_commands


class WorkingGroups(commands.Cog):
    """A cog that manages users adding themslves and leaving Working Groups"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_commands.command(name="working-group")
    async def affinity_group(self, interaction):
        for k, v in interaction.data.options.items():
            if v.name == "join":
                add = True
                action = "joined"
            else:
                add = False
                action = "left"
            
            result = await _add_remove_from_group(interaction.guild, interaction.author, v.value, "working groups",  add)

            if result is True:
                msg_content = f":white_check_mark: You have successfully {action} the {v.value} working group channel.\
                \nIf there was an error, please contact an admin."
            else:
                msg_content = ":x: Sorry, there was an error. Please try again or contact an admin."
            
        await interaction.reply(
            content=msg_content,
            hide_user_input=True,
            ephemeral=True,  # Only visible to the invoker of the command
            type=4,  # Immediate response with acknowledge
        )


class AffinityGroups(commands.Cog):
    """A cog that manages users adding themselves and leaving Affinity Groups"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_commands.command(name="affinity-group")
    async def affinity_group(self, interaction):
        for k, v in interaction.data.options.items():
            if v.name == "join":
                add = True
                action = "joined"
            else:
                add = False
                action = "left"
            
            result = await _add_remove_from_group(interaction.guild, interaction.author, v.value, "affinity groups",  add)

            if result is True:
                msg_content = f":white_check_mark: You have successfully {action} the {v.value} affinity group channel.\
                \nIf there was an error, please contact an admin."
            else:
                msg_content = ":x: Sorry, there was an error. Please try again or contact an admin."
            
        await interaction.reply(
            content=msg_content,
            hide_user_input=True,
            ephemeral=True,  # Only visible to the invoker of the command
            type=4,  # Immediate response with acknowledge
        )


async def _add_remove_from_group(guild, user, channel_name: str, category_name: str,  add: bool) -> bool:
    """Helper function to add or remove a user from a specific channel.
    If add is false, it will remove the permissions."""

    category = discord.utils.get(guild.categories, name=category_name)
    channel = discord.utils.get(guild.channels, category_id=category.id, name=channel_name)
    if add is True:
        await channel.set_permissions(user, read_messages=add, send_messages=add, add_reactions=add,
            read_message_history=add, external_emojis=add, attach_files=add, embed_links=add)
    else:
        # Resets the permissions for the user and removes the channel-specific override
        await channel.set_permissions(user, overwrite=None)
    return True


def setup(bot: commands.Bot) -> None:
    """Load Affinity and Working Groups cogs"""
    bot.add_cog(AffinityGroups(bot))
    bot.add_cog(WorkingGroups(bot))
