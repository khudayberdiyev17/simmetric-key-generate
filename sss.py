import secrets
import os
os.system("cls")

def decimalToBinary(n): 
    return bin(n).replace("0b", "") 

len = int(input("Kalit uzunligini kiriting: "))

random_key = secrets.randbits(len)
print (decimalToBinary(random_key))
