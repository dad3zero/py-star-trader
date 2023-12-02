from pystartrader import settings
from pystartrader.startrader import game

if not settings.GAME_DB.exists():
    from pystartrader.setup import setup
    setup.do_setup()

game.start()