import math
import enum

class EvolutionLevel(enum.Enum):
    """
    Work in progress: use enums for levels
    """
    COSMOPOLITAN = 15
    DEVELOPED = 10
    UNDERDEVELOPED = 5
    FRONTIER = 0


class GeoPoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def coordinates(self):
        return self._x, self._y

    def with_x(self, x):
        return GeoPoint(x, self.y)

    def with_y(self, y):
        return GeoPoint(self.x, y)

    def distance_to(self, other):
        """

        :param x: x coordinate to the destination
        :param y: y coordinate to the destination
        :return:
        :rtype: int
        """

        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

class Star:
    """
    Describes a star (world) in the game
    """

    def __init__(self, name: str,
                 level: EvolutionLevel,
                 x: int, y: int,
#                 stardate: StarDate,
                 image: str = None):
        """

        :param name: name of the star
        :param level: Evolution level of the star
        :param x:
        :param y:
        :param stardate:
        """
        self.name = name
        self.level = level

        self._coordinates = GeoPoint(x, y)

#        self.stardate = stardate

        self._image = image

        # Following data should move to an economy object
        self.merchandises = [0, 0, 0, 0, 0, 0]
        self.prices = [0, 0, 0, 0, 0, 0]
        self.prods = [0, 0, 0, 0, 0, 0]  # productivity / month

    @property
    def x(self):
        return self._coordinates.x

    @property
    def y(self):
        return self._coordinates.y

    def __str__(self):
        return f"Star {self.name} ({self.x:3}, {self.y:3})"
