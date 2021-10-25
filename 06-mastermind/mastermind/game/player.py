from game.move import Move
class Player():
    def __init__(self, name):
        self._name = name 
        self._move = Move("0000")

    def set_name(self):
        return self._name

    def get_name(self):
        """Returns the player's name.
        Args:
            self (Player): an instance of Player.
        """
        return self._name

    def get_move(self):
        """
        Returns the player's last move(an instance of move hasn't
        moved yet this method returns None.
        """

        return self._move
    
    def set_move(self, move):
        self._move = move