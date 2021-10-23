import random
class Board():
    def __init__(self):
        self._player_move = {}
        self._code = []
        self._generate_code()
        self.won_game = False

    def _generate_code(self):
        for i in range(4):
            self._code.append(random.randint(0,9))

    def to_string(self):
        text = ""
        text += "-----------------------\n"
        for name in self._player_move.keys():
            text += f"Player {name}: "
            move = self._player_move[name]
            text += f"{move.get_guess_string()} "
            # text += f"{self.hint}\n"
        text += "-----------------------\n"

    def check_guess(self, player):
        name = player.get_name()
        move = player.get_move()
        if move == self._code:
            self.won_game = True
        else:
            self.won_game = False
        hint = self._create_hint(move)
        # self._board[name] = [move, hint]


    def _create_hint(self, guess):
        hint = ""
        for index, letter in enumerate(guess):
            if self.code[index] == letter:
                hint += "x"
            elif letter in self.code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def populate_player(self, player):
        name = player.get_name()
        move = player.get_move()
        self._player_move[name] = move