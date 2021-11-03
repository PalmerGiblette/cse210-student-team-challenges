from game.console import Console
from game.board import Board
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director():
    def __init__(self):
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        # self._move = None
        self._roster = Roster()

    
    def start_game(self):
        self._setup_game()
        while self._keep_playing:
            self._do_inputs()
            self._do_updates()
            self._do_output()

    def _do_inputs(self):
        player = self._roster.get_current()
        self._console.write(f'{player.get_name()}\'s turn: ')
        guess = self._console.read('Please input a code: ')
        
        move = Move(guess)
        
        player.set_move(move)
        
        

    def _do_updates(self):
        player = self._roster.get_current()
        move = player.get_move()
        self._board.check_guess(move)
        self._keep_playing = self._board.won_game
        print(self._board._create_hint(move))
    
    def _do_output(self):
        if self._board.won_game == False:
            player = self._roster.get_current()
            self._console.write(f'{player.get_name()} won!')
        
        #hopfuly prints out the updated board LOL
        board = self._board.to_string()
        self._console.write(board)
        
        self._roster.next_player()

    def _setup_game(self):
        board = "---------\n"
        for n in range(2):
            name = self._console.read(f'Enter a name for player {n + 1}: ')
            player = Player(name)
            board += f"Player {name}: ----, ****\n"

            self._board.populate_player(player)
            self._roster.add_player(player)
        board += f"-------\n"

        self._console.write("")

        self._console.write(board)
