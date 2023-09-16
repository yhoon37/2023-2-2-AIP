

sum=0   #전체합을 저장할 변수

for i in range(1000000):    #1부터 백만까지 반복
    if (i%2 == 0):      #짝수일경우 그냥 넘어감
        pass        
    else:               #홀수인 경우
        for j in range(6):
            sum += i%10     #1의 자리 숫자를 더함
            i = int(i/10)   #숫자에 10을 나눠서 다음 자리숫자를 더할수 있게 함
            if(i==0):       #숫자가 0이되면 반복 종료
                break

            
#출력 형식에 맞게 출력
print("The sum of the digits of odd numbers")
print("from 1 to one million is {:,}.".format(sum))