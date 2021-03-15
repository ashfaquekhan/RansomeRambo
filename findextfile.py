import os
path = ('D:\\')
print("Counting all .txt files in: " + path)
x=0

for files in os.listdir(path):
    if files.endswith('.txt'):
        x+=1
        print("\nFile #" + str(x) + ": " + files)
print("\nTotal number of .txt files in: " + path + " -")
print(x)