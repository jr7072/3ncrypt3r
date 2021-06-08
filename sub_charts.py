import random
import sys
from string import digits, ascii_letters, punctuation
from itertools import product
from getpass import getpass

def shuffle(arr):

    last_index = len(arr) - 1

    while last_index > 0:

        rand_index = random.randint(0 , last_index)
        temp = arr[last_index]
        arr[last_index] = arr[rand_index]
        arr[rand_index] = temp
        last_index -= 1

    return arr

def key_generator():

    key_characters = list(digits + ascii_letters + punctuation)
    key_length = 8
    key_list = []
    
    for i in range(key_length):
        
        o = random.randint(0, len(key_characters) - 1)
        key_list.append(key_characters[o])
    
    return "".join(key_list)

def substitution_key_generator(list_1, list_2):

    chart = {}

    list_1 = shuffle(list_1)
    list_2 = shuffle(list_2)
    index_1 = 0
    index_2 = 0
    
    for i in range(len(list_1)):

        chart[list_1[index_1]] = list_2[index_2]
        index_1 += 1
        index_2 += 1
    
    return chart

def substitute(arr, chart):
    
    for i in range(len(arr)):

        arr[i] = chart[arr[i]]
    
    return arr

def storage(chart, values, keys):

    save_name = input("Input file name:\n")
    save_name = save_name + ".txt"
    
    
    with open(save_name, "w") as f:
        
        for key, value in chart.items():
            
            f.write(key + value + "\n")
        
        f.write(values)
    
    with open("s3cr3t.txt", "a") as f:

        f.write("\n" + save_name + ":" + keys)

def retrieve_chart(file_name):

    
    chart = {}
    
    with open(file_name, "r") as f:

        lines = f.readlines()
        lines = "".join(lines)
        lines = lines.split("\n")
    
    encryption = lines.pop(-1)
    
    for x in lines:

        chart[x[1]] = x[0]
    
    
    return chart, encryption


def decryption(chart, encryption):

    
    encryption = [x for x in encryption]
   
    i = 0
    
    for x in encryption:

        encryption[i] = chart[encryption[i]]
        i += 1

    sorted_encryption = reverse_grid(encryption)
    sorted_encryption.reverse()
    

    return "".join(sorted_encryption)


def reverse_grid(value):

    i = 1
    x_1 = []

    if len(value) % 2 != 0:

        last_value = value.pop(0)
        
        
        for x in value:

            x_1.append(value[i])
            value.pop(i)
            i += 1
        
        sorted_value = x_1 + value
        sorted_value.append(last_value)
    
    else:

        for x in value:

            x_1.append(value[i])
            value.pop(i)
            i += 1
        
        sorted_value = x_1 + value
    
    return sorted_value

def auth(file_name):
    
    file_name = file_name + ".txt"
    
    try:
        
        with open("s3cr3t.txt", "r") as f:

            lines = f.readlines()
            lines = "".join(lines)
            lines = lines.split("\n")
    
        for x in lines:

            if file_name in x:

                file_data = x
    
        file_data = file_data.split(":")
   
        auth = False
        count = 0
        key = getpass("Enter key:\n")
        
        while auth == False:

            if key == file_data[1]:
            
                auth = True
            
        
            elif key != file_data[1]:

                print("wrong key!")
                key = getpass("enter key:\n")
                count += 1
            

            if count == 5:

                print("you have attempted the max number of tries!")
                quit = input("press ENTER to quit:\n")
                break
    
        if auth == True:

            chart, encryption = retrieve_chart(file_name)
            value = decryption(chart, encryption)
        
        
    
    except:

        value = "File name not found!"
    
    return value

def Encrypt(value):

    board = [x for x in value]
    encrypt = []
    counter = 1
    width = len(board) // 2
    
    board.reverse()
    
    if len(board) % 2 == 0:

        for i in range(0,width):

            encrypt.append(board[width - 1 + counter])
            encrypt.append(board[i])
            counter += 1
        
    else:

        encrypt.append(board[-1])

        for i in range(0, width):

            encrypt.append(board[width - 1 + counter])
            encrypt.append(board[i])
            counter += 1
    
    list_1 = list(digits + ascii_letters + punctuation + " ")
    list_2 = list(digits + ascii_letters + punctuation + " ")

    chart = substitution_key_generator(list_1, list_2)   
    encrypt = substitute(encrypt, chart)

    return  "".join(encrypt), chart  





