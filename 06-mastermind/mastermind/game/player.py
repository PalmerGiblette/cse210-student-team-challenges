class Player():
    def __init__(self, name):
        self._name = name 
        self._move = None

    def set_name(self):
        return self._name