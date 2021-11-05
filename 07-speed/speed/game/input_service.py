import sys
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        #self._screen = screen
        
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        key_int = raylibpy.get_key_pressed()
        

        key_string = None

        if key_int != -1:
            
            if key_int == 32:
                return '*'
            else:
                key_string = chr(key_int)

        return key_string
    
    def window_should_close(self):
        """
        Determines if the user is trying to close the window
        """
        return raylibpy.window_should_close()