class Console:
    def __init__(self):
        self.image = [
            ' ___  ',
            '/___\ ',
            '\   / ',
            ' \ /  ',
            '  0   ',
            ' /|\  ',
            ' / \  ',
            '       ',
            '^^^^^^ ',
            ]
    
    def draw_parachute(self, num_fail):
        '''
        Draws man and the remaining parachute he has.
        '''
        for i in range(num_fail, len(self.image)):
            print(self.image[i])

    def draw_death(self):
        '''
        Draws death scene for when player loses.
        '''
        print('  x  ')
        for i in range(5, len(self.image)):
            print(self.image[i])
    



