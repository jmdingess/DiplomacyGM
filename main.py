import logging
import os

from bot import bot

# from test import test_adjudication_mapping

log_level = logging.getLevelNamesMapping().get(os.getenv("log_level", "INFO"))
if not log_level:
    log_level = logging.INFO
logging.basicConfig(level=log_level)

bot.run()
# test_adjudication_mapping.run()
