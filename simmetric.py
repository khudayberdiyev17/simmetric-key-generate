from cryptography.fernet import Fernet
import os
os.system("cls")

OchiqMatn = input("Matn kiriting: ")
os.system("cls")



key = Fernet.generate_key()



fernet = Fernet(key)


encMessage = fernet.encrypt(OchiqMatn.encode())

print("Ochiq Matn: ", OchiqMatn)
print("Shifr Matn: ", encMessage)


decMessage = fernet.decrypt(encMessage).decode()

print("Ochiq Matn: ", decMessage)

