

def main():
    statesList = createListFromFile("States.txt")
    createSortedFile(statesList, "StatesAlpha.txt")

def createListFromFile(fileName):
    infile = open(fileName, 'r')
    desiredList = [line.rstrip() for line in infile]
    infile.close()
    return desiredList

def createSortedFile(listName, fileName) :
    listName.sort()
    for i in range(len(listName)):
        listName[i] = listName[i] + "\n"
    outfile = open(fileName, 'w')
    outfile.writelines(listName)
    outfile.close()
main()

##Altering Items in a Text File
import os.path

if os.path.isfile("ABC.txt"):
    print("file already exists.")
else:
    infile = open("ABC.txt", 'w')
    infile.write("a\nb\nc\n")
    infile.close()

##Sets