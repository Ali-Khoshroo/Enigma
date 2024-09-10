def get_plug_board():
    print("______________________________________________________________________")
    print(f"Plug Board :\nWhich letters do you want to change ? (10 pairs Maximum)\ntype letters with nothing between(example : RB)then press enter\nwhen you are done just type in Done")
    print("______________________________________________________________________")

    user_pb = []
    while True:

        user_input = input("==>")

        if user_input.lower() == "done" or len(user_pb) == 9 :
            break
        else : 
            while len(user_input) > 2 :
                print("Please Enter two letters at a time...")
                user_input = input("==>")
            x = user_input.upper()
            user_pb.append(x)

    return user_pb


def get_rotors():
    print("______________________________________________________________________")
    print(f"Rotors :\nType the Number of the Rotor you want to choose then press enter\nFormat => I = Rotor wiring , Notch\n\n> 1) I = EKMFLGDQVZNTOWYHXUSPAIBRCJ , Q\n> 2) II = AJDKSIRUXBLHWTMCQGZNPYFVOE , E\n> 3) III = BDFHJLCPRTXVZNYEIWGAKMUSQO , V\n> 4) IV = ESOVPZJAYQUIRHXLNFTGKDCMWB , J\n> 5) V = VZBRGITYUPSDNHLXAWMJQOFECK , Z ")
    print("______________________________________________________________________")

    valid_options = ["1", "2", "3", "4", "5"]
    user_rotor = input("First Rotor : ")
    while user_rotor not in valid_options :
        print("Invalid Option !")
        user_rotor = input("First Rotor : ")

    user_rotor_2 = input("Second Rotor : ")
    while user_rotor_2 not in valid_options :
        print("Invalid Option !")
        user_rotor_2 = input("Second Rotor : ")

    user_rotor_3 = input("Third Rotor : ")
    while user_rotor_3 not in valid_options :
        print("Invalid Option !")
        user_rotor_3 = input("Third Rotor : ")

    return int(user_rotor)-1,int(user_rotor_2)-1,int(user_rotor_3)-1


def get_reflector():
    print("______________________________________________________________________")
    print(f"Reflector :\nChose The Reflector\n> 1) A = EJMZALYXVBWFCRQUONTSPIKHGD\n> 2) B = YRUHQSLDPXNGOKMIEBFZCWVJAT\n> 3) C = FVPJIAOYEDRZXWGCTKUQSBNMHL")
    print("______________________________________________________________________")

    user_reflector = input("Enter The Reflector : ").upper()
    while user_reflector not in ["1","2","3"] :
        print("Invalid Option !")
        user_reflector = input("Enter The Reflector : ").upper()
        
    return int(user_reflector)-1


def get_message_key():
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

    return user_msg_key


def get_message():
    print("______________________________________________________________________")
    print(f"Message  :")
    user_message = input("Enter the text you want to encrypt :")
    print("______________________________________________________________________")

    return user_message

