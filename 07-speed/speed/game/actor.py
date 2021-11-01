from game import constants
from game.coordinate_point import Point

class Actor:
    '''
    Any visible, dynamic thing that participates in the game. Actor tracks
    the appearance, coordinates, and velocity of an object in the 2d game space.
    '''
    def __init__(self):
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._width = 0
        self._height = 0
        