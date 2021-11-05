from game.actor import Actor
from game.input_service import InputService
from game.coordinate_point import CoordinatePoint

class Buffer(Actor):
    
    def __init__(self):
        super().__init__()
        self._buffer = ["", ""]
        self.set_position(CoordinatePoint(50, 550))
        self._input_service = InputService()

    def update_text(self):
        letter = self._input_service.get_letter()
        if letter != None:
            self._buffer += letter
            self.set_text(self._buffer)


    def is_enter_pressed(self):
        return self._buffer[-1] == '*'

    def find_matches(self, word_list):
        length = len(word_list)
        matches = [False]*length
        for i in length:
            word_class = word_list[i]
            word = word_class.get_word()
            if word in self._buffer:
                matches[i] = True
        self._buffer = ''
        return matches

        