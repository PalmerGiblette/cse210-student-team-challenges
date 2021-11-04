#from speed.game.actor import Actor


from game.actor import Actor
from game.constants import constants
import random

class WordEntity(Actor):

    def __init__(self):
        self._position = (0,0)
        self._velocity = (0,0)
        self._word = ""
        self.populate_word()
    
    def populate_word(self):
        self._position = (constants.MAX_X, random.randint(0, constants.MAX_Y))
        self._velocity = (random.randit(1, constants.MAX_Y), 0)
        self._word = random.choice(constants.Library)


    def get_word(self):
        word = self._word
        return word

    def get_word_velocty(self):
        velocity = self._velocity
        return velocity

    def get_word_position(self):
        position = self._position
        return position