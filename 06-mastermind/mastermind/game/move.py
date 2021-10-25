class Move():
    def __init__(self, guess_str):
        self._guess_list = [int(x) for x in guess_str]

    def get_guess_list(self):
        return self._guess_list

    def get_guess_string(self):
        text = ""
        for number in self._guess_list:
            text += str(number)
        return text