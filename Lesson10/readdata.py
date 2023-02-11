import os
#This is how you read a data from a datafile in a txt file
# with open("datafile.txt", "r") as readdata:
#     print(readdata.read())

#This is how you write something into the datafile in a txt file
with open("datafile.txt", "a+") as writedata:
    inputwords = input()
    writedata.write(f"\n{inputwords}")
    

with open("datafile.txt", "r") as readdata:
    os.system("clear")
    print(readdata.read())