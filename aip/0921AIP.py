def g(x):
    return (int(x)**2) 

def say(msg, times=1):
    print(msg*times)

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

def main():
    ##List Comprehhension
    # list1 = ['2', '3','4','5']
    # list = [g(x) for x in list1] 
    # print(list)
    # print([ord(x) for x in "abc"])
    # print([x**2 for x in range(3)])
    
    ##Default Argument VAlues, keyword Arguments
    #say("hi", 5)
    #func(c=50, a=100)

    ##Lambda Expression
    names = ["Dennis Ritchie", "Alan Kay", "John Backus", "James Gosling"]
    names.sort(key=lambda name: name.split()[-1])   #lambda대신 function을 선언하여 해도 됨
    nameString = ", ".join(names)
    print(nameString)

    ##Reading Tet Files
    file = "datas/FirstPresidents.txt"
    displayWithForLoop(file)
    print()
    displayWithListComprehension(file)
    print()
    displayWithReadline(file)

    ##Creating TextFiles
    L = ["George Washington", "John Adams", "Thomas Jefferson"]
    outfile = open("FirstPresidents2.txt", 'w')
    createWithWrite(L, outfile)
    outfile = open("FirstPresidents3.txt", 'w')
    createWithWritelines(L, outfile)

def displayWithForLoop(file):
    infile = open(file, 'r')
    for line in infile:
        print(line.rstrip())
    infile.close()
def displayWithListComprehension(file):
    infile = open(file, 'r')
    listPres = [line.rstrip() for line in infile]
    infile.close()
    print(listPres)

def displayWithReadline(file):
    infile = open(file, 'r')
    line = infile.readline()
    while line != "":
        print(line.rstrip())
        line = infile.readline()
    infile.close()

def createWithWrite(L, outfile):
    for i in range(len(L)):
        outfile.write(L[i] | "\n")
    outfile.close()
def createWithWritelines(outfile):
    for i in range(len(L)):
        L[i] = L[i] + "\n"
    outfile.writelines(L)
    outfile.close()

main()