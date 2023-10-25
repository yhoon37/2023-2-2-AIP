#list를 입력받는다
mylist = eval(input("Enter measurements as a list: "))

#list를 오름차순으로 정렬한다
mylist.sort()

#입력 받은 리스트의 크기를 구한다.
listLen = len(mylist)
halfLen = int(listLen/2)
median = 0.0

if(listLen%2 == 0):     #짝수개일 경우
    #median은 두개의 중간값의 평균
    median = (mylist[halfLen - 1] + mylist[halfLen])/2
    
else:                   #홀수개일 경우
    #median이 중간값이 된다
    median = mylist[halfLen]

#출력한다
print("Median: {0:.1f}".format(median))

