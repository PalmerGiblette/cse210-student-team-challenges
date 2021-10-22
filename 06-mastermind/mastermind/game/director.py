<<<<<<< HEAD
from game.console import Console()
from game.board import Board()
from game.move import Move()
from game.player import Player()
from game.roster import Roster()
=======
from game.console import Console
from game.board import Board
from game.move import Move
from game.player import Player
from game.roster import Roster
>>>>>>> 4b8d9da6ef1d7c9e0f039bad9680fbe57535c7ca

class Director():
    def __init__(self):
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._move = None
        self._roster = Roster()
    
    def start_game(self):
        self._setup_game()
        while self._keep_playing:
            self._do_inputs()
            self._do_updates()
            self._do_output()

    def _do_inputs(self):
        board = self._board.to_string()
        self._console.write(board)
<<<<<<< HEAD

        player = self._roster.get_current()
        self._console.write(f'{player.get_name()}\'s turn: ')
        guess = self._console.read_number('>')
=======
        player = self._roster.get_current()
        self._console.write(f'{player.get_name()}\'s turn: ')
        guess = self._console.read('>')
        guess = guess.split(guess)
        for i in guess:
            guess[i] = int(guess[i])
>>>>>>> 4b8d9da6ef1d7c9e0f039bad9680fbe57535c7ca
        move = Move(guess)
        player.set_move(move)

    def _do_updates(self):
        player = self._roster.get_current()
<<<<<<< HEAD
        self._board.check_guess(player.get_move())
=======
        self._board.check_guess(player)
>>>>>>> 4b8d9da6ef1d7c9e0f039bad9680fbe57535c7ca
    
    def _do_output(self):
        if self._board.won_game:
            player = self._roster.get_current()
            self._console.write(f'{player.get_name()} won!')
        
        self._roster.next_player()

    def _setup_game(self):
        for n in range(2):
            name = self._console.read(f'Enter a name for player {n + 1}')
            player = Player(name)
<<<<<<< HEAD
            self._roster.add_player(player)
            
            
=======
            self._board.populate_player(player)
            self._roster.add_player(player)
>>>>>>> 4b8d9da6ef1d7c9e0f039bad9680fbe57535c7ca
