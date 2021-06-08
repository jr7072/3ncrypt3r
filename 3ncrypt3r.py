import sys
import random
import sub_charts
from string import digits, ascii_letters, punctuation
from getpass import getpass

def main():


    print("-" * 50)
    print("Welcome to my first Encryption tool powered by python 3.6")
    print("The program will encrypt a message and provide you with a key.")
    print("Run the program again and choose the dycrypt option to dycrypt a message")
    print("-" * 50)
    
    value = ""
    
    valid = False
    
    while valid == False:
        
        option = input("choose to dycrypt or encrypt (D/E):\n")
        
        if option == "E":
            
            valid = True
            E_string = getpass("input message to encrypt:\n")
            value = value + E_string
            
        elif option == "D":
            
            valid = True
            user_file = input("Input message file name to Dycrypt:\n")
            
            
        
        elif option == "Q":

            valid = True
            sys.exit()        
            
        
        else:

            print("invalid entry choose to Decrypt or encrypt (D/E // Q to quit):\n")
    
    if len(value) > 0:

        encryption, chart = sub_charts.Encrypt(value)
        
        print("-" * 50)
        print("Your encryption is:", encryption)
        print("-" * 50)   
        
        key = sub_charts.key_generator()
        sub_charts.storage(chart, encryption, key)
        
        print("-" * 50)
        print("Your key is:", key)
        print("Keep it safe!!!")
        print("-" * 50)
        print("Thanks for using my encryption program.")
        print("-" * 50)
        quit = input("press ENTER to quit:\n")
    
    elif len(value) == 0:

        try:
            
            answer = sub_charts.auth(user_file)
            print(answer)
            quit = input("press ENTER to quit:\n")
        
        except:
            quit = input("press ENTER to quit:\n")
            sys.exit()

    



main()


