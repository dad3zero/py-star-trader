import random


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
