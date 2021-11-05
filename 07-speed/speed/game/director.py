import raylibpy
from game import constants
from game.score_board import ScoreBoard
from game.buffer import Buffer
from game.word_entity import WordEntity

class Director:
    '''
    A code template for a person who directs the game. The responsibility
    of this class of objetcs is to control the sequence of play.

    Stereotype:
        controller

    Atributes:
        todo: fill this in lol
    '''
    def __init__(self, output_service, input_service):
        self._keep_playing = True
        self._output_service = output_service
        self._input_service = input_service
        self._score_board = ScoreBoard()
        self._buffer = Buffer()
        self._words_list = []

    def start_game(self):
        '''
        starts the game loop to control the sequence of play.

        args:
            self (director): an instance of Director.
        '''
        print("Launching Speed....")
        self._output_service.open_window("Speed")

        self._populate_words()

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game end!")

    def _get_inputs(self):
        letter = self._input_service.get_letter()
        self._buffer.update_text(letter)

    def _do_updates(self):
        
        self._update_words()
        

    def _do_outputs(self):
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._words_list)
        self._output_service.draw_actor(self._score_board)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()

    def _populate_words(self):
        """
        generates a data structure that creates the initial 5 words 
        """
        for _ in range(0, constants.STARTING_WORDS):
            word = WordEntity()
            self._words_list.append(word)
        

    def _update_words(self):
        """
        updates the words in the list as they leave the screan or they get removed by the player
        """
        for i in range(len(self._words_list)):
            word = self._words_list[i]
            word.move_next()
            if word.edge_of_screen():
                self._score_board.subtract_points(word.get_points())
                word.populate_word()

        if self._buffer.is_enter_pressed():
            matches = self._buffer.find_matches(self._words_list)
            
            for i in range(len(matches)):
                if matches[i]:
                    word = self._words_list[i]
                    self._score_board.add_points(word.get_points())
                    word.populate_word()