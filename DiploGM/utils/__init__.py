import logging

import discord
from discord import Guild, Thread
from discord.abc import GuildChannel
from discord.ext import commands

from .sanitise import simple_player_name

from DiploGM import config
from DiploGM.manager import Manager
from DiploGM.models.player import Player

logger = logging.getLogger(__name__)


def get_role_by_player(player: Player, roles: Guild.roles) -> discord.Role | None:
    for role in roles:
        if simple_player_name(role.name) == simple_player_name(player.name):
            return role
    return None


def get_player_by_channel(
    channel: commands.Context.channel,
    manager: Manager,
    server_id: int,
    ignore_category=False,
) -> Player | None:
    # thread -> main channel
    if isinstance(channel, Thread):
        channel = channel.parent

    board = manager.get_board(server_id)
    name = channel.name
    if (not ignore_category) and not config.is_player_category(channel.category.name):
        return None

    if board.is_chaos() and name.endswith("-void"):
        name = name[:-5]
    else:
        if not name.endswith(config.player_channel_suffix):
            return None

        name = name[: -(len(config.player_channel_suffix))]

    try:
        return board.get_cleaned_player(name)
    except ValueError:
        pass
    try:
        return board.get_cleaned_player(simple_player_name(name))
    except ValueError:
        return None

    return None


# FIXME this is done pretty poorly
async def get_channel_by_player(
    player: Player, ctx: commands.Context, manager: Manager
) -> GuildChannel:
    guild = ctx.guild
    guild_id = guild.id
    board = manager.get_board(guild_id)

    channel_name = simple_player_name(player.name) + config.player_channel_suffix

    for category in guild.categories:
        if not config.is_player_category(category.name) and not board.is_chaos():
            continue

        for channel in category.channels:
            if channel.name == channel_name:
                return channel

    return None


def get_player_by_name(name: str, manager: Manager, server_id: int) -> Player | None:
    for player in manager.get_board(server_id).players:
        if simple_player_name(player.name) == simple_player_name(name):
            return player
    return None


def get_maps_channel(guild: Guild) -> GuildChannel | None:
    for channel in guild.channels:
        if (
            channel.name.lower() == "maps"
            and channel.category is not None
            and channel.category.name.lower() == "gm channels"
        ):
            return channel
    return None


def get_orders_log(guild: Guild) -> GuildChannel | None:
    for channel in guild.channels:
        # FIXME move "orders" and "gm channels" to bot.config
        if (
            channel.name.lower() == "orders-log"
            and channel.category is not None
            and channel.category.name.lower() == "gm channels"
        ):
            return channel
    return None


def is_player_channel(player_role: str, channel: commands.Context.channel) -> bool:
    player_channel = player_role + config.player_channel_suffix
    return simple_player_name(player_channel) == simple_player_name(
        channel.name
    ) and config.is_player_category(channel.category.name)


from .logging import log_command, log_command_no_ctx
from .send_message import send_message_and_file
from .orders import get_orders, get_filtered_orders
from .map_archive import upload_map_to_archive
from .sanitise import (
    sanitise_name,
    simple_player_name,
    get_keywords,
    _manage_coast_signature,
    get_unit_type,
    parse_season,
    get_value_from_timestamp
)
