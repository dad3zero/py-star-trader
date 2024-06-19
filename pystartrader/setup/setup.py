import random
import itertools
from enum import Enum
import logging

from pystartrader.startrader import galaxy
from pystartrader import settings

Cycle = Enum("Cycle", ["NORTH", "EAST", "SOUTH", "WEST"])

locations = {galaxy.EvolutionLevel.FRONTIER: (50, 100, 50, 100),
             galaxy.EvolutionLevel.DEVELOPED: (0, 50, 0, 50),
             galaxy.EvolutionLevel.UNDERDEVELOPED: (0, 100, 0, 100),
             galaxy.EvolutionLevel.COSMOPOLITAN: (0, 0, 0, 0),
             }

def create_original_starsystem(star_names: list[str], max_stars=4):
    """
    Create a starsystem according to the original article.

    This creation suppose a 100x100 surface game.

    First planet, SOL is at the center of the map (0, 0).

    Class II planets are created in the 50x50 center box, class IV outside of this box. Class III
    are sprinkled throughout.

    Stars are placed clockwise, first star (after SOL) is placed on the upper side (y > 0), second
    on the left (x > 0), third on the lower (y < 0) fourth on the left (x < 0) and we cycle again.

    The program should place 2 class IV planets then one class III. Then, the program should cycle
    through class IV, III, II and place as many planets as the setup asks for.

    The minimum distance between planets must be 15 units. If less, we toss again.

    :param star_names: Names of
    :param max_stars: Number of stars to create, must be at least 4
    :raises ValueError: if max_stars < 4 or less star names than expected stars.
    """
    stars = []
    if max_stars < 4:
        raise ValueError(f'There should be at least 4 stars, got {max_stars}')

    if len(star_names) < max_stars:
        raise ValueError(f"Not enough names in list for the number of created stars ({len(star_names)} for {max_stars} stars")

    star_names = star_names.copy()  # Working on a copy to avoid destruction on referenced data

    stars.append(galaxy.Star(star_names.pop(0),
                             galaxy.EvolutionLevel.COSMOPOLITAN,
                             0, 0))

    random.shuffle(star_names)
    star_names = star_names[:max_stars - 1]
    cycle_cycler = itertools.cycle(Cycle.__members__.items())

    add_star(stars, star_names.pop(0), galaxy.EvolutionLevel.FRONTIER, next(cycle_cycler)[1])
    add_star(stars, star_names.pop(0), galaxy.EvolutionLevel.FRONTIER, next(cycle_cycler)[1])
    add_star(stars, star_names.pop(0), galaxy.EvolutionLevel.UNDERDEVELOPED, next(cycle_cycler)[1])

    planets_level = [galaxy.EvolutionLevel.FRONTIER, galaxy.EvolutionLevel.UNDERDEVELOPED, galaxy.EvolutionLevel.DEVELOPED]

    for name, level, cycle in zip(star_names, itertools.cycle(planets_level), cycle_cycler):
        add_star(stars, name, level, cycle[1])

    return stars


def create_star(name: str, level, cycle=None):
    min_x, max_x, min_y, max_y = locations[level]
    x = random.randint(min_x, max_x)
    y = random.randint(min_y, max_y)

    if cycle:
        if cycle is Cycle.NORTH:
            x = -x if random.randint(-1, 1) < 0 else x

        elif cycle is cycle.EAST:
            y = -y if random.randint(-1, 1) < 0 else y

        elif cycle is cycle.SOUTH:
            x = -x if random.randint(-1, 1) < 0 else x
            y = -y

        elif cycle is cycle.WEST:
            x = -x
            y = -y if random.randint(-1, 1) < 0 else y

    return galaxy.Star(name, level, x, y)

def add_star(starsystem:list[galaxy.Star], name:str, level, cycle):
    is_valid = False
    while not is_valid:
        new_star = create_star(name, level, cycle)
        is_valid = validate_star_distances(new_star, starsystem)

    logging.debug("New star %s created", new_star)
    starsystem.append(new_star)


def validate_star_distances(new_star: galaxy.Star, stars:list[galaxy.Star]):
    for star in stars:
        if abs(star.x - new_star.x) < 15 or abs(star.y - new_star.y) < 15:
            return False

    return True

def do_setup():
    star_system = create_original_starsystem(settings.STAR_NAMES, 8)
    return star_system


def get_sol_coordinates():
    """
    Create coordinates for SOL which should be the central star.

    :return: a tuple of coordinates, (0, 0)
    """
    return 0, 0


def get_random_developed_class_coordinates(map_size=100):
    """
    Creates a new class II star coordinates. A class II star appears in the
    central half of the box.

    :param map_size: Size of the map with the historical value as default.
    :return: a tuple of coordinates with values from -25 to 25
    """
    inner_zone = map_size / 2
    x = round(random.random() * inner_zone - (inner_zone / 2))
    y = round(random.random() * inner_zone - (inner_zone / 2))

    return x, y


def get_random_underdeveloped_class_coordinates(map_size=100):
    """
    Creates a new class III star coordinates. A class III star appears anywhere.

    :return: a tuple of coordinates with values from -50 to 50
    """
    x = round(random.random() * map_size - (map_size / 2))
    y = round(random.random() * map_size - (map_size / 2))

    return x, y


def get_random_frontier_class_coordinates():
    """
    Creates a new class IV star coordinates. A class IV star appears outside
    the central 50 ly box.

    :return: a tuple of coordinates with values from -50 to -25 or 25 to 50.
    """
    x = random.random()
    x = round((x if x > 0.5 else x - 1) * 50)

    y = random.random()
    y = round((y if y > 0.5 else y - 1) * 50)

    return x, y
