def main():
 ## Analyze monthly payment of mortgage. 
 annualRateOfInterest, monthlyPayment, begBalance = inputData() 
 (intForMonth, redOfPrincipal, endBalance) =  calculateValues(annualRateOfInterest, monthlyPayment, begBalance)
 displayOutput(intForMonth, redOfPrincipal, endBalance)

def inputData():
    """데이터 들을 입력받고 그 값들을 return 한다"""
    annualRateOfInterest = eval(input("annual rate of interest: "))
    monthlyPaymet = eval(input("Enter monthly payment: "))
    begBalance = eval(input("Enter beg. of month balance: "))
    return (annualRateOfInterest, monthlyPaymet, begBalance)

def calculateValues(annualRateOfInterest, monthlyPayment, begBalance):
    """문제 조건에 맞게 값들을 계산한다"""
    intForMonth = annualRateOfInterest/12/100.0 * begBalance
    redOfPrincipal = monthlyPayment - intForMonth
    endBalance = begBalance - redOfPrincipal

    return(intForMonth, redOfPrincipal, endBalance)

def displayOutput(intForMonth, redOfPrincipal, endBalance):
    """출력형식에 맞게 값들을 출력한다"""
    print("Interest paid for the month: ${:,.2f}".format(intForMonth))
    print("Reduction of principal: ${:,.2f}".format(redOfPrincipal))
    print("End of month balacne: ${:,.2f}".format(endBalance))

main()
