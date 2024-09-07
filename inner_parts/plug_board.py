import string
class PlugBoard():

    def __init__(self,switched_letters):

        self.right = string.ascii_uppercase
        self.left = string.ascii_uppercase
        
        for sl in switched_letters:
            item_1 = sl[0]
            item_2 = sl[1]
            position_item_1 = self.right.find(item_1)
            position_item_2 = self.right.find(item_2)
            self.left = self.left[:position_item_1] + item_2 + self.left[position_item_1+1:] 
            self.left = self.left[:position_item_2] + item_1 + self.left[position_item_2+1:]


    def forward(self,position):
        letter = self.right[position]
        position = self.left.find(letter)
        return position
    
    def backward(self,position):
        letter = self.left[position]
        position = int(position)
        position = self.right.find(letter)
        return position
    
