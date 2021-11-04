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
        '''
        starts the game loop to control the sequence of play.

        args:
            self (director): an instance of Director.
        '''
        print("Launching Speed....")
        self._output_service.open_window("Speed")

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game end!")

    def _get_inputs(self):
        pass

    def _do_updates(self):
        pass

    def _do_outputs(self):
        pass

    def _populate_words(self):
        pass

    def _update_words(self):
        pass
        