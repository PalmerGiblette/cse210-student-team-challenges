import random
class Board():
    def __init__(self):
        self._player_move = {}
        self._code = []
        self._generate_code()
        print(self._code)
        self.won_game = False
        self.hint = ""

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
            text += f"{self.hint}\n"
        text += "-----------------------\n"
        return text

    def check_guess(self, guess):
        move = guess.get_guess_list()
        if move == self._code:
            self.won_game = False
            
        else:
            self.won_game = True
            


    def _create_hint(self, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        move = guess.get_guess_list()
        code = self._code
        self.hint = ""
        for index, letter in enumerate(move):
            if code[index] == letter:
                self.hint += "x"
            elif letter in code:
                self.hint += "o"
            else:
                self.hint += "*"
        return self.hint

                                                    

    def populate_player(self, player):
        name = player.get_name()
        move = player.get_move()
        self._player_move[name] = move