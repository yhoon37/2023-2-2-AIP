
#가격을 입력받고 eval 함수를 통해 int나 flaot형으로 변환
purchase_price = eval(input("Enter purchase price: "))   
selling_price = eval(input("Enter selling price: "))

#문제에 맞게 값을 구함
markup = selling_price - purchase_price
percentage_markup = markup/purchase_price*100
profit_margin = markup/selling_price*100

#출력 형식에 맞게 출력
print("Markup: ${:.1f}".format(markup))     
print("Percentage markup: {:.1f}%".format(percentage_markup))
print("Profit margin: {:.2f}%".format(profit_margin))