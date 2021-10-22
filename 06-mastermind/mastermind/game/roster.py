class Roster():
    def __init__(self):
        """
        Class constructor.
        
        args:"""
        self.current -1
        self.players = []

    def get_current(self):
        
        return self.players[self.current]

    def add_player(self, player):
        """
        Adds the given player to the roster
        """

        if player not in self.players:
            self.players.append(player)