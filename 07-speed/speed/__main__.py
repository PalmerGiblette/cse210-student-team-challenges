import os

from game.director import Director
from game.output_service import OutputService


def main():
    output_service = OutputService()
    director = Director(output_service)
    director.start_game()

if __name__ == "__main__":
    main()