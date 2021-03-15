import string
from ctypes import windll
from glob import glob
import os
global totalFiles
global totalDir
totalDir=0
totalFiles=0

def read_drives(drive):
    for base, dirs, files in os.walk(drive):
        print('Searching in : ',base)
        for directories in dirs:
            for Files in files:
                print(Files)


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives 

if __name__ == '__main__':
    lis = get_drives() 
    print(lis)
    read_drives(lis[0]+':\\')