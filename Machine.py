from inner_parts.key_lamp import KeyBoard_Lamp as kl
from inner_parts.plug_board import PlugBoard as pb
from inner_parts.rotors import Rotor as rt
from inner_parts.reflector import Reflector as rf
from inner_parts.encipher import Encipher
from UI import *



# KeyBoard 
key_board = kl


# PlugBoard
plug_board = pb(get_plug_board())


# Rotors Wiring
I = rt("EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q")
II = rt("AJDKSIRUXBLHWTMCQGZNPYFVOE","E")
III = rt("BDFHJLCPRTXVZNYEIWGAKMUSQO","V")
IV = rt("ESOVPZJAYQUIRHXLNFTGKDCMWB","J")
V = rt("VZBRGITYUPSDNHLXAWMJQOFECK","Z")
all_rotors = [I , II , III , IV , V] 


# Reflector Wiring
reflector_A = rf("EJMZALYXVBWFCRQUONTSPIKHGD")
reflector_B = rf("YRUHQSLDPXNGOKMIEBFZCWVJAT")
reflector_C = rf("FVPJIAOYEDRZXWGCTKUQSBNMHL")
all_reflectors = [reflector_A, reflector_B, reflector_C]


# Defining the Enigma mashine
chosen_rotors = get_rotors()
machine = Encipher(key_board,plug_board,all_rotors[chosen_rotors[0]],all_rotors[chosen_rotors[0]],all_rotors[chosen_rotors[0]],all_reflectors[get_reflector()])

# Seting the keys
machine.set_keys(get_message_key())


# Encipher a letter
message = get_message()
encrypted_text = ""
for item in message :
    if item == " " :
        encrypted_text = encrypted_text + " "
    elif item.isnumeric():
        encrypted_text = encrypted_text + item
    else : 
        encrypted_text = encrypted_text + (machine.encipher_command(item.upper()))


print(f"Original Message --> {message}\nEncrypted Message --> {encrypted_text}\n")



