from discord.ext import commands


async def _has_role_check(ctx: commands.Context, guild, *role_names: str) -> bool:
    """Checks if the user has a specific role within the server"""
    member = guild.get_member(int(ctx.author.id))

    for role in member.roles:
        if role.name in role_names:
            return True
    return False
