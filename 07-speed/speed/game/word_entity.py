#from speed.game.actor import Actor
from game.actor import Actor
from game import constants
from game.coordinate_point import CoordinatePoint
import random

class WordEntity(Actor):

    def __init__(self):
        super().__init__()
        self.populate_word()
        self._word = ""
        self._points = 0
    
    def populate_word(self):
        length = random.randint(0, constants.MAX_Y)
        velocity = -1 * (random.randint(1, constants.MAX_VELOCITY))
        self.set_position(CoordinatePoint(constants.MAX_X, length))
        self.set_velocity(CoordinatePoint(velocity, 0))
        self._word = random.choice(constants.LIBRARY)
        self.set_text(self._word)

        self._points = len(self._word)

    def get_points(self):
        return self._points

    def get_word(self):
        word = self._word
        return word

    def get_word_velocty(self):
        velocity = self._velocity
        return velocity

    def get_word_position(self):
        position = self._position
        return position

    def edge_of_screen(self):
        x = self.get_position().get_x()

        return x <= -30