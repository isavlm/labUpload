def collectDailyWorkHours():
    print("Gathering daily hours worked, please input 0 if there wasn't any work done that day.")
    myHours = []
    for i in range(5):
        myDailyHours = input("Please input the hours worked: ")
        if not myDailyHours.isdigit():
            print("Only numerical inputs accepted")
        else:
            myHours.append(myDailyHours)
    return myHours

def calculateTotalHours(listOfHours):
    myTotalHours = 0
    for i in listOfHours:
        myTotalHours += int(i)
    return myTotalHours

def calculateOverTime(hours):
    myOverTime = 0
    if hours > 40:
        print("Calculating overtime hours...")
        myOverTime = hours - 40
        print(f"Total overtime hours: {myOverTime}")
    return myOverTime

def calculateOverTimePay(hourlyRate):
     return hourlyRate * 1.5

def writeResults(hourlyRate,totalHours,overTimePay):
    myFile = open("payRate.txt","w")
    myFile.write(f"at an hourly rate of {hourlyRate} the {totalHours} worked includes {overTimePay} in overtime pay")

def myMainFunction():
    myHourlyRate = input("Please input the hourly rate of the employee: ")
    if myHourlyRate.isdigit():
        myHoursWorked = collectDailyWorkHours()
        myTotalHours = calculateTotalHours(myHoursWorked)
        myOvertimeHours = calculateOverTime(myTotalHours)
        if myOvertimeHours > 0:
            myOvertimePayRate = calculateOverTimePay(int(myHourlyRate))
            myOvertimePay = myOvertimeHours * myOvertimePayRate
            myRegularPay = int(myHourlyRate) * 40
            myFinalPay = myOvertimePay + myRegularPay
            print(f"Total amount paid for this week is: {myFinalPay}" )
        else:
            print("There isn't any overtime for the employee this week.")
            myRegularPay = int(myHourlyRate) * int(myTotalHours)
            print(f"Total amount paid for this week is: {myRegularPay}")
        myFile = open("EmployeeHourlyRate.txt","x")
        writeResults(myHourlyRate,myTotalHours,myOvertimePay)
    else:
        print("Hourly rate must be a numerical value, try again!")
        myMainFunction()    
myMainFunction()