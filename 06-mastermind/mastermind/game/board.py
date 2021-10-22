import random
class Board():
    def __init__(self):
        self._board = []
        self.code = []
        self._generate_code()
        self.won_game = False
        self.hint = ""
        

    def _generate_code(self):
        for i in range(5):
            self.code.append(random.randint(0,9))

    def to_string(self):
        text = ""
        text += "-----------------------\n"
        for name in self._board:
            text += f"Player {name}: "
            text += "----"
            text += f"{self.hint}\n"
        text += "-----------------------\n"

    def check_guess(self, player):
        name = player.get_name()
        move = player.get_move()
        if move == self.code:
            self.won_game = True
        hint = self._create_hint(move)
        self._board[name] = [move, hint]

    def _create_hint(self, guess):
        hint = ""
        for index, letter in enumerate(guess):
            if self.code[index] == letter:
                hint += "x"
            elif letter in self.code:
                hint += "o"
            else:
                hint += "*"
        return self.hint

    def populate_player(self, player):
        self._board.append(player.get_name())