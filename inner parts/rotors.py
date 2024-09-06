import string

class Rotor():

    def __init__(self,wiring,notch):

        self.left = string.ascii_uppercase
        self.right = wiring
        self.notch = notch



    def forward(self,position):
        letter = self.right[position]
        position = self.left.find(letter)
        return position
    
    def backward(self,position):
        letter = self.left[position]
        position = int(position)
        position = self.right.find(letter)
        return position
    
    def rotation(self):
        self.left = self.left[1:] + self.left[0]
        self.right = self.right[1:] + self.right[0]

    def rotate_to_letter(self,letter):
        letter_position = self.left.find(letter)
        
        for i in range(letter_position) :
            self.rotation()

    # To show the Rotors current formation
    def show(self):
        print(self.left)
        print(self.right)
        print("")
            
            

