from inner_parts.key_lamp import KeyBoard_Lamp as kl
from inner_parts.plug_board import PlugBoard as pb
from inner_parts.rotors import Rotor as rt
from inner_parts.reflector import Reflector as rf
from inner_parts.encipher import Encipher



# User Interface

print("______________________________________________________________________")
print(f"Plug Board :\nWhich letters do you want to change ?\ntype letters with nothing between(example : RB)then press enter\nwhen you are done just type in <Done>")
print("______________________________________________________________________")

user_pb = []
while True:

    plug_input = input("==>")

    if plug_input.lower() == "done" :
        break
    else : 
        while len(plug_input) > 2 :
            print("Please Enter two letters at a time...")
            plug_input = input()
        x = plug_input.upper()
        user_pb.append(x)




print("______________________________________________________________________")
print(f"Rotors :\nType the Number of the Rotor you want to chose then press enter\nFormat => I = Rotor wiring , Notch\n\n> 1) I = EKMFLGDQVZNTOWYHXUSPAIBRCJ , Q\n> 2) II = AJDKSIRUXBLHWTMCQGZNPYFVOE , E\n> 3) III = AJDKSIRUXBLHWTMCQGZNPYFVOE , V\n> 4) IV = ESOVPZJAYQUIRHXLNFTGKDCMWB , J\n> 5) V = VZBRGITYUPSDNHLXAWMJQOFECK , Z ")
print("______________________________________________________________________")

valid_options = ["1", "2", "3", "4", "5"]
user_rotor = input("First Rotor : ")
while user_rotor not in valid_options :
    print("Invalid Value !")
    user_rotor = input("First Rotor : ")

user_rotor_2 = input("Second Rotor : ")
while user_rotor_2 not in valid_options :
    print("Invalid Value !")
    user_rotor_2 = input("Second Rotor : ")

user_rotor_3 = input("Third Rotor : ")
while user_rotor_3 not in valid_options :
    print("Invalid Value !")
    user_rotor_3 = input("Third Rotor : ")



print("______________________________________________________________________")
print(f"Reflector :\nChose The Reflector\n> 1) A = EJMZALYXVBWFCRQUONTSPIKHGD\n> 2) B = YRUHQSLDPXNGOKMIEBFZCWVJAT\n> 3) C = FVPJIAOYEDRZXWGCTKUQSBNMHL")
print("______________________________________________________________________")

user_reflector = input("Enter The Reflector : ").upper()
while user_reflector not in ["1","2","3"] :
    print("Invalid Value !")
    user_reflector = input("Enter The Reflector : ").upper()



print("______________________________________________________________________")
print(f"Message Key :\nSet The Message Key (Example = MBD)")
print("______________________________________________________________________")

user_msg_key = input("Enter The Key : ").upper()
while len(user_msg_key) > 3 :
    print("Please Enter 3 Letters for Key ! ")
    user_msg_key = input("Enter The Key : ").upper()
    while user_msg_key.isalpha() == False :
        print("Invalid Value ! ")
        user_msg_key = input("Enter The Key : ").upper()



print("______________________________________________________________________")
print(f"Message  :")
user_message = input("Enter the text you want to encrypt :")



    

# KeyBoard 
test_kb = kl


# PlugBoard
test_pb = pb(user_pb)


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
test = Encipher(test_kb,test_pb,all_rotors[int(user_rotor)-1],all_rotors[int(user_rotor_2)-1],all_rotors[int(user_rotor_3)-1],all_reflectors[int(user_reflector)-1])

# Seting the keys
test.set_keys(user_msg_key)


# Encipher a letter
message = user_message
encrypted_text = ""
for item in message :
    if item == " " :
        encrypted_text = encrypted_text + " "
    elif item.isnumeric():
        encrypted_text = encrypted_text + item
    else : 
        encrypted_text = encrypted_text + (test.encipher_command(item.upper()))

print("===============================================\n")
print(f"Original Message --> {message}\nEncrypted --> {encrypted_text}")









