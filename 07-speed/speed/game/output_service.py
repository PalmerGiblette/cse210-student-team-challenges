from game import constants
import raylibpy

class OutputService:
    '''
    Handles outputting the game state to the player, this class
    draws the game state to the terminal.
    '''
    def __init__(self):
        pass

    def open_window(self, title):
        '''
        opens the game window with the game title
        '''
        raylibpy.init_window(constants.MAX_X, constants.MAX_Y, title)
        raylibpy.set_target_fps(constants.FRAME_RATE)