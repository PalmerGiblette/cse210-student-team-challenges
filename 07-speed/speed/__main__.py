import os
os.environ['RAYLIB_BIN_PATH'] = r'raylib-2.0.0-Win64-mingw\lib'

from game.director import Director
from game.output_service import OutputService
from game.input_service import InputService


def main():
    output_service = OutputService()
    input_service = InputService()
    director = Director(output_service, input_service)
    director.start_game()

if __name__ == "__main__":
    main()