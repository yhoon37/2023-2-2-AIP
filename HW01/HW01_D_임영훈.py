
coefficient = eval(input("Enter coefficient of restitution: "))
height = eval(input("Enter initial height in meters: "))

bounce = 0      #튕기는 횟수를 저장하는 변수
up = 0.0        #올라가는 높이를 저장하는 변수
total = 0.0     #전체 이동거리를 저장하는 변수

is_down = True  #내려가는지 올라가는지를 알려주는 변수

while(True):
    if(is_down):                    #내려가면
        total += height             #높이만큼 전체 이동거리에 더한다
        up = height*coefficient     #다음에 올라올 높이를 계산한다
        is_down = False     

    else:
        bounce += 1         #bounce 횟수를 1 증가시킨다
        if(up>=0.1):        #10cm이상이면 다시 올라간다
            total += up     #올라온 거리만큼 전체 이동거리에 더한다
            height = up     #올라온 거리가 높이가 된다
            is_down = True
        else:               
            break           #10cm미만이면 반복을 종료한다

#출력 형식에 맞게 출력
print("Number of bounces: {}".format(bounce))
print("Meters traveled: {:.2f}".format(total))