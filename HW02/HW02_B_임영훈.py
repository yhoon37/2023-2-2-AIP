specialNum = 0

#10,000부터 99,999까지 반복
for i in range(10000, 100000):
    num = str(i)                #int형을 string으로 바꿈
    reverseNum = str(i*4)       #num*4 값도 string으로 바꿈
    
    listNum = list(num)         #string에는 reverse method가 없기때문에 list로 바꿈
    listNum.reverse()           #숫자를 역순으로 바꿈
    
    
    #역순으로 저장한 숫자를 join method를 이용하여 string으로 만들어줌
    if(''.join(listNum) == reverseNum):     #두 문자열를 비교하여 같은지 확인
        specialNum = i          #조건을 만족하면 현재 i가 우리가 원하던 숫자가 됨
        break                   #반복을 종료

#출력
print("Since 4 x {} is {},".format(specialNum, specialNum*4))
print("the special number is {}.".format(specialNum*4))

#if(''.join(listNum) == reverseNum): 대신에
#if(num[::-1] == reverseNum): 해도 동일함
