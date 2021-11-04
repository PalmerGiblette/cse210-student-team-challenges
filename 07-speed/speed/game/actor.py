from game import constants
from game.coordinate_point import CoordinatePoint

class Actor:
    '''
    Any visible, dynamic thing that participates in the game. Actor tracks
    the appearance, coordinates, and velocity of an object in the 2d game space.
    '''
    def __init__(self):
        self._text = ""
        self._position = CoordinatePoint(0, 0)
        self._velocity = CoordinatePoint(0, 0)
    
    def get_position(self):
        return self._position
    
    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text
    
    def get_velocity(self):
        return self._velocity

    def move_next(self):
        x = self._position.get_x()
        y = self._position.get_y()
        dx = self._velocity.get_x()
        dy = self._velocity.get_y()
        self._position = CoordinatePoint(x + dx, y + dy)

    def set_position(self, position):
        self._position = position
    
    def set_velocity(self, velocity):
        self._velocity = velocity