# Enigma
An Enigma machine is a famous encryption machine used by the Germans during WWII to transmit coded messages. An Enigma machine allows for billions and billions of ways to encode a message, making it incredibly difficult for other nations to crack German codes during the war ( for a time the code seemed unbreakable ).

## Why was Enigma so hard to break?
The number of permutations of settings available to the encoders made the Enigma code difficult to break. The operator set the machine’s rotating wheels and plugboard to different predetermined positions according to daily orders, regularly changing the cipher.

## Mathematical analysis
Combining three rotors from a set of five, each of the 3 rotor settings with 26 positions, and the plugboard with ten pairs of letters connected, the military Enigma has `158,962,555,217,826,360,000` different settings ( *nearly 159 quintillion or about 67 bits* ).

## How my code works
### First Run `Machine.py`    
The machine has a number of settings. You give the settings to the machine and then your message.   
The machine encrypts the message and if you enter the encrypted message ,decrypts it ( The setting should be the exact same to decrypt the message )   
### Settings that you can use :   
+ *plugboard :*  
The plugboard has `26 letters` and you can switch up to `10 pairs` of letters  
+ *Rotors :*  
There are `5 Rotors`  which you can choose `3` of them  
+ *Reflector :*  
There are `3 reflectors` which you can choose `1`  
+ *Message Key :*  
It is a `3 letter key` ( example : CWF )

