import logging

from discord.ext import commands
import random

from discord.ext.commands import (
    ExtensionNotFound,
    ExtensionNotLoaded,
    ExtensionAlreadyLoaded,
    NoEntryPointError,
    ExtensionFailed,
)

from bot.config import (
    IMPDIP_SERVER_ID,
    IMPDIP_BOT_WIZARD_ROLE,
    ERROR_COLOUR,
    PARTIAL_ERROR_COLOUR,
    IMPDIP_SERVER_BOT_STATUS_CHANNEL_ID,
)
from bot.bot import DiploGM
from bot import perms
from bot.utils import send_message_and_file
from diplomacy.persistence.manager import Manager

logger = logging.getLogger(__name__)
manager = Manager()


class DevelopmentCog(commands.Cog):
    """
    Superuser features primarily used for Development of the bot
    """

    bot: DiploGM

    def __init__(self, bot: DiploGM):
        self.bot = bot

    @commands.command(hidden=True)
    @perms.superuser_only("show the superuser dashboard")
    async def su_dashboard(self, ctx: commands.Context):

        extensions_body = ""
        for extension in self.bot.get_all_extensions():
            if extension in self.bot.extensions.keys():
                extensions_body += "- :white_check_mark: "
            else:
                extensions_body += "- :x: "
            extensions_body += f"{extension}\n"

        cogs_body = ""
        for cog in self.bot.cogs.keys():
            cogs_body += f"- {cog}\n"

        bot_wizards = (
            self.bot.get_guild(IMPDIP_SERVER_ID)
            .get_role(IMPDIP_BOT_WIZARD_ROLE)
            .members
        )
        footer = random.choice(
            [f"Rather upset at {bot_wizard.nick} >:(" for bot_wizard in bot_wizards]
            + [
                f"eolhc keeps {random.choice(['murdering', 'stabbing'])} me",
                f"aahoughton, I don't recognise your union!",
            ]
        )

        await send_message_and_file(
            channel=ctx.channel,
            title=f"DiplomacyGM Dashboard",
            fields=[("Extensions", extensions_body), ("Loaded Cogs", cogs_body)],
            footer_content=footer,
        )

    @commands.command(hidden=True)
    @perms.superuser_only("unloaded extension")
    async def extension_unload(self, ctx: commands.Context, extension: str):
        try:
            await self.bot.unload_diplogm_extension(extension)
        except ExtensionNotFound:
            status=f"Extension was not found"
            colour=ERROR_COLOUR
        except ExtensionNotLoaded:
            status = f"Extension was not loaded"
            colour=PARTIAL_ERROR_COLOUR
        else:
            status = f"Unloaded Extension"
            colour = None
        finally:
            await send_message_and_file(
                channel=ctx.channel,
                embed_colour=colour,
                title=f"{status}: {extension}"
            )

    @commands.command(hidden=True)
    @perms.superuser_only("load extension")
    async def extension_load(self, ctx: commands.Context, extension: str):
        try:
            await self.bot.load_diplogm_extension(extension)
        except ExtensionNotFound:
            status = "Extension was not found"
            colour = ERROR_COLOUR
        except ExtensionAlreadyLoaded:
            status = "Extension was already loaded"
            colour = PARTIAL_ERROR_COLOUR
        except NoEntryPointError:
            status = "Extension has no setup function"
            colour = ERROR_COLOUR
        except ExtensionFailed:
            status = "Extension failed to load"
            colour = ERROR_COLOUR
        else:
            status = "Loaded extension"
            colour = None
        finally:
            await send_message_and_file(
                channel=ctx.channel,
                embed_colour=colour,
                title=f"{status}: {extension}"
            )

    @commands.command(hidden=True)
    @perms.superuser_only("reload extension")
    async def extension_reload(self, ctx: commands.Context, extension: str):
        try:
            await self.bot.reload_diplogm_extension(extension)
        except ExtensionNotFound:
            status=f"Extension was not found: {extension}"
            colour=ERROR_COLOUR
        except ExtensionNotLoaded:
            status=f"Extension was not loaded: {extension}",
            colour=PARTIAL_ERROR_COLOUR
        except ExtensionAlreadyLoaded:
            status=f"Extension was unload but could not be loaded as it was already loaded: {extension}",
            colour=PARTIAL_ERROR_COLOUR
        except NoEntryPointError:
            status=f"Extension was unloaded but now has no setup function: {extension}",
            colour=ERROR_COLOUR
        except ExtensionFailed:
            status=f"Extension failed to load: {extension}",
            colour=ERROR_COLOUR
        else:
            status=f"Reloaded Extension"
            colour=None
        finally:
            await send_message_and_file(
                channel=ctx.channel,
                embed_colour=colour,
                title=f"{status}: {extension}"
            )

    @commands.command(hidden=True)
    @perms.superuser_only("shutdown the bot")
    async def shutdown_the_bot_yes_i_want_to_do_this(self, ctx: commands.Context):
        await send_message_and_file(
            channel=ctx.channel, title=f"Why would you do this to me?", message=f"Shutting down"
        )
        channel = self.bot.get_channel(IMPDIP_SERVER_BOT_STATUS_CHANNEL_ID)
        if channel:
            await channel.send(f"{ctx.author.mention} stabbed me")
        await self.bot.close()


async def setup(bot: DiploGM):
    cog = DevelopmentCog(bot)
    await bot.add_cog(cog)


async def teardown(bot: DiploGM):
    pass
