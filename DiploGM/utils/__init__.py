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
