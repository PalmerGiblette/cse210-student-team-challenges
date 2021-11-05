import os

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