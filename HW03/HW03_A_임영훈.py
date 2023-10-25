import os.path

fileName = "Names.txt"                  #파일이름을 Names.txt로 설정한다

def main():
    mySet = readSetFromFile()
    name = inputName()
    modifiedSet = insertSet(mySet, name)
    writeToFile(modifiedSet)

def readSetFromFile(): # implement functions
    if(os.path.isfile(fileName)):           #Names.txt라는 파일이 있다면
        infile = open(fileName, 'r')        #파일을 read모드로 열고

        #파일에 들어 있는 이름들을 끝에 있는 개행문자를 제거하여 set에 넣어준다
        mySet = {name.rstrip() for name in infile}  
        
        infile.close()                      #파일을 닫는다
        
        return mySet                        #앞에서 만든 set을 return 한다
    
    else:                               #만약 Names.txt라는 파일이 없다면
        print("{} does not exist.".format(fileName))    #파일이 없다는 메세지를 출력하고
        print("Terminate program.")
        exit()                          #프로그램을 종료한다.

def inputName():
    name = input("Enter a first name to be included: ") #이름을 입력받고
    return name                         #입력받은 이름을 return한다

def insertSet(mySet, name):
    
    if name in mySet:       #이름이 set에 있다면
        print("{} is already in {}".format(name, fileName)) #이미 있다는 메세지를 출력한다
    else:                   #이름이 set에 없다면
        print("{} is added in {}".format(name, fileName))   #이름을 추가하였다는 메세지를 출력한다.
        mySet.add(name)     #set에 이름을 추가한다
    
    return mySet        

def writeToFile(modifiedSet):
    modifiedList = list(modifiedSet)    #입력받은 set을 list로 바꿔준다
    modifiedList.sort()                 #list를 정렬한다.
    f = open(fileName, 'w')             #파일을 write모드로 연다
    f.write('\n'.join(modifiedList))    #list에 있는 name들에 개행문자를 붙여 전체 한 문자열로 만들고 파일에 쓴다
    f.close()                           #파일을 닫는다     
main()