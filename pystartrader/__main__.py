from pystartrader import settings
from pystartrader.startrader import game
import logging

from pystartrader import settings

logging.info("New game started")

if not settings.GAME_DB.exists():
    from pystartrader.setup import setup
    star_system = setup.do_setup()

game.start(star_system)