
import os 
flub = raw_input('Where would you like your save directory to be?')

file = open("datafile.txt", "r")
filedata = file.read()
file.close()

try:
    if os.stat("datafile.txt").st_size > 0:
        print("Value exists already")
else():
    file = open("datafile.txt", "w")
    file.write(flub)
    file.close()
    print("flub value updated to: " + flub)
except(OSError):
    print("No file")