#salary를 입력 받음
salary = eval(input("Enter beginning salary: "))

new_salary = salary*(1.05*1.05*1.05*1.05)       #5%인상을 4번함
change_percentage = ((new_salary/salary)-1)*100 #실제 인상 퍼센트를 구함

#출력 형식에 맞게 출력
print("New salary: ${:,.2f}".format(new_salary))
print("Cahnge: {:.2f}%".format(change_percentage))