from key_lamp import KeyBoard_Lamp as kl
from plug_board import PlugBoard as pb
from rotors import Rotor as rt
from reflector import Reflector as rf
from encipher import Encipher



# KeyBoard 
test_kb = kl


# PlugBoard
test_pb = pb(["AB","CD","EF"])


# Rotors Wiring
I = rt("EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q")
II = rt("AJDKSIRUXBLHWTMCQGZNPYFVOE","E")
III = rt("AJDKSIRUXBLHWTMCQGZNPYFVOE","V")
IV = rt("ESOVPZJAYQUIRHXLNFTGKDCMWB","J")
V = rt("VZBRGITYUPSDNHLXAWMJQOFECK","Z")


# Reflector Wiring
reflector_A = rf("EJMZALYXVBWFCRQUONTSPIKHGD")
reflector_B = rf("YRUHQSLDPXNGOKMIEBFZCWVJAT")
reflector_C = rf("FVPJIAOYEDRZXWGCTKUQSBNMHL")


# Defining the Enigma mashine
test = Encipher(test_kb,test_pb,I,II,III,reflector_A)

# Seting the keys
test.set_keys("WTF")


# Encipher a letter
message = "hello 23 world "
encrypted_text = ""
for item in message :
    if item == " " :
        encrypted_text = encrypted_text + " "
    elif item.isnumeric():
        encrypted_text = encrypted_text + item
    else : 
        encrypted_text = encrypted_text + (test.encipher_command(item.upper()))


print(f"Original Message --> {message}\nEncrypted --> {encrypted_text}")
















# GUI part







