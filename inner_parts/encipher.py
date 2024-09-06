class Encipher():

    def __init__(self,KeyBoard,PlugBoard,Rotor_1,Rotor_2,Rotor_3,Reflector):

        self.KeyBoard = KeyBoard
        self.PlugBoard = PlugBoard
        self.Rotor_1 = Rotor_1
        self.Rotor_2 = Rotor_2
        self.Rotor_3 = Rotor_3
        self.Reflector = Reflector
        self.counter_1 = 0
        self.counter_2 = 0
        

    def set_keys(self, key):
        self.Rotor_1.rotate_to_letter(key[0])
        self.Rotor_2.rotate_to_letter(key[1])
        self.Rotor_3.rotate_to_letter(key[2])


    def encipher_command(self,letter):
        
        
        if self.Rotor_2.left[0] == self.Rotor_2.notch :

            self.Rotor_1.rotation()
            self.Rotor_2.rotation()
            self.Rotor_3.rotation()
            
        elif self.Rotor_1.left[0] == self.Rotor_1.notch :
            self.Rotor_1.rotation()
            self.Rotor_2.rotation()
            
        else :
            self.Rotor_1.rotation()
            
            
        kl_out = self.KeyBoard.forward(letter)
        pb_out = self.PlugBoard.forward(kl_out)
        rt_out = self.Rotor_1.forward(pb_out)
        rt2_out = self.Rotor_2.forward(rt_out)
        rt3_out = self.Rotor_3.forward(rt2_out)
        rf_out = self.Reflector.reflect(rt3_out)
        rt3_out = self.Rotor_3.backward(rf_out)
        rt2_out = self.Rotor_2.backward(rt3_out)
        rt_out = self.Rotor_1.backward(rt2_out)
        pb_out = self.PlugBoard.backward(rt_out)
        final = self.KeyBoard.backward(pb_out)
        return final


        
