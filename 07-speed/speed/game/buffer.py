from game.actor import Actor
from game.coordinate_point import CoordinatePoint

class Buffer(Actor):
    
    def __init__(self):
        super().__init__()
        self._buffer = " "
        self.set_position(CoordinatePoint(50, 550))
        self.set_buffer()


    def update_text(self, letter):
        if letter != None:
            self._buffer += letter
            self.set_buffer()


    def is_enter_pressed(self):
        return self._buffer[-1] == '*'

    def find_matches(self, word_list):
        length = len(word_list)
        matches = [False]*length
        for i in range(length):
            word_class = word_list[i]
            word = word_class.get_word()
            if word in self._buffer:
                matches[i] = True
        self._buffer = ' '
        self.set_buffer()
        return matches

    def set_buffer(self):
        self.set_text(f"Buffer: {self._buffer}")

        