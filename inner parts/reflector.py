import string

class Reflector():

    def __init__(self,wiring):

        self.left = string.ascii_uppercase
        self.right = wiring
        
    def reflect(self,position):
        letter = self.right[position]
        position = int(position)
        position = self.left.find(letter)
        return position