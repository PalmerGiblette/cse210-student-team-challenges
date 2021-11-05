import os

MAX_X = 800
MAX_Y = 600
FRAME_LENGTH = 0.08
FRAME_RATE = 30
STARTING_WORDS = 5
MAX_VELOCITY = 10
WORD_KILL_ZONE = -30
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
