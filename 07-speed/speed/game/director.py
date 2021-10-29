import raylibpy
from game import constants
from game.score_board import ScoreBoard
from game.buffer import Buffer

class Director:
    '''
    A code template for a person who directs the game. The responsibility
    of this class of objetcs is to control the sequence of play.

    Stereotype:
        controller

    Atributes:
        todo: fill this in lol
    '''
    def __init__(self, input_service, output_service):
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score_boar = ScoreBoard()
        self._snake = Buffer()

    def start_game(self):
        #todo: fill this in
        pass