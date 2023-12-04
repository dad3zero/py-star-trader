from pystartrader.startrader.galaxy import EvolutionLevel
from pystartrader.setup.setup import create_star

def test_SOL_creation():
    star = create_star("test", EvolutionLevel.COSMOPOLITAN)

    assert star.x == 0
    assert star.y == 0
    assert star.name == "test"
    assert star.level == EvolutionLevel.COSMOPOLITAN

def test_frontier_creation():
    star = create_star("test", EvolutionLevel.FRONTIER)

    assert 50 <= star.x <= 100
    assert 50 <= star.y <= 100
    assert star.name == "test"
    assert star.level == EvolutionLevel.FRONTIER
