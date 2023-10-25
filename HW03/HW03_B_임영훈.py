filename = "Units.txt"

def main():
    feet = populateDictionary()
    orig, dest, length = getInput()
    ans = length * feet[orig] / feet[dest]
    print("Length in {0}: {1:,.4f}".format(dest, ans))

def populateDictionary():
    f = open(filename, 'r')     #파일을 read 모드로 연다.
    feet ={}                    #dictionary하나를 선언한다.
    for line in f:              #파일을 한줄씩 읽는다
        data = line.split(',')  #콤마로 구분하여 데이터 리스트로 만든다
        feet[data[0]] = eval(data[1])   #dictionary에 key-value 쌍을 추가해준다.
    
    f.close()                   #파일을 닫는다.
    return feet                 #새로 만든 dictionary를 return 한다.

def getInput():
    orig = input("Unit to convert from: ")      #original unit을 입력받는다
    dest = input("Unit to convert to: ")        #destination unit을 입력받는다
    length = eval(input("Enter length in {}: ".format(orig)))   #original unit으로 길이를 입력받는다

    return (orig, dest, length)                 #입력받은 값들을 return 한다.
main()