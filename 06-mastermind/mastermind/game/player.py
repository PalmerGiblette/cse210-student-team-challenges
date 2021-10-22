class Player():
    def __init__(self, name):
        self._name = name 
        self._move = None

    def set_name(self):
        return self._name

    def get_name(self):
        """Returns the player's name.
        Args:
            self (Player): an instance of Player.
        """
        return self._name