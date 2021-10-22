class Console():
    def __init__(self):
        pass

    def write(self, input):
        """
        Prints whatever is given to it 
        """
        print(input)
        

    def read_number(self, message):
        """
        gets user input from the user and returns a number
        """
        return int(input(message))

    def read(self, message):
        """
        gets user input and returns a string
        """
        return input(message)