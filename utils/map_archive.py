import asyncio
import os

from subprocess import PIPE
from discord.ext import commands
from DiploGM.diplomacy.adjudicator.utils import svg_to_png
from DiploGM.diplomacy.persistence import phase
from DiploGM.diplomacy.persistence.board import Board

from utils import log_command, send_message_and_file


async def upload_map_to_archive(ctx: commands.Context, server_id: int, board: Board, map: str, turn: tuple[str, phase] | None = None) -> None:
    if "maps_sas_token" not in os.environ:
        return
    if turn is None:
        turnstr = f"{(board.year + board.year_offset) % 100}{board.phase.shortname}"
    else:
        turnstr = f"{int(turn[0]) % 100}{turn[1].shortname}"
    url = None
    with open("gamelist.tsv", "r") as gamefile:
        for server in gamefile:
            server_info = server.strip().split("\t")
            if str(server_id) == server_info[0]:
                url = f"{os.environ['maps_url']}/{server_info[1]}/{server_info[2]}/{turnstr}m.png{os.environ['maps_sas_token']}"
                break
    if url is None:
        return
    png_map, _ = await svg_to_png(map, url)
    p = await asyncio.create_subprocess_shell(
        f'azcopy copy "{url}" --from-to PipeBlob --content-type image/png',
        stdout=PIPE,
        stdin=PIPE,
        stderr=PIPE,
    )
    data, error = await p.communicate(input=png_map)
    error = error.decode()
    await send_message_and_file(
        channel=ctx.channel,
        title=f"Uploaded map to archive",
    )
    log_command(
        logger,
        ctx,
        message=(
            f"Map uploading failed: {error}"
            if len(error) > 0
            else "Uploaded map to archive"
        ),
    )
