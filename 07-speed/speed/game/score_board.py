from game.actor import Actor
from game.coordinate_point import CoordinatePoint

class ScoreBoard(Actor):
    '''
    Handles score of player
    '''
    def __init__(self):
        super().__init__()
        self._points = 0
        position = CoordinatePoint(1,0)
        self.set_position(position)
        self.set_text(f"Score: {self._points}")
    
    def add_points(self, points):
        self._points += points
        self.set_text(f"Score: {self._points}")

    def subtract_points(self,points):
        self._points -= points
        self.set_texts(f"Score: {self._points}")