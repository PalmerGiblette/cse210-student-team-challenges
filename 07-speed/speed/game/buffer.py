from game.actor import Actor
from game.input_service import InputService
from game.coordinate_point import CoordinatesPoints

class Buffer(Actor):
    
    def __init__(self):
        super().__init__()
        self._buffer = ''
        self.set_position(Point())
        self._input_service = InputService()

    def update_text(self):
        letter = self._input_service.get_letter()
        self._buffer += letter
        self.set_text(self._buffer)

    def is_enter_pressed(self):
        return self._buffer[-1] == '*'

    def find_match(self, word_list):
        matches = []
        for word in word_list:
            if word in self._buffer:
                matches.append(word)
        self._buffer = ''
        return matches

        