import time 

def standardDeviation():
    num = 0
    valueTotal = 0
    values = []

    numOfValues = int(input("\nEnter the number of values: "))

    while True:
        value = float(input("What is value #" + str(num + 1) + "? "))
        values.append(value)
        print(values)
        num += 1
        if num != numOfValues:
            continue
        else:
            break

    for a in values:
        valueTotal += a

    daAverage = valueTotal / numOfValues

    time.sleep(2)
    print(" ")
    print("The total of all values is " + str(valueTotal) + "\n")
    print("Therefore, " + str(valueTotal) + " / " + str(numOfValues) + " = " + str(daAverage) + "\n")

    time.sleep(4)
    print("We found the average. Now, let's find the variance. \n")

    variList = []
    variValues = 0
    for v in values:
        variValues = v - daAverage
        variList.append(variValues)
    
    time.sleep(3)
    print("First, we subtract all the values by the average:")
    print(variList)
    print(" ")

    variSList = []
    for vs in variList:
        vs **= 2
        variSList.append(vs)
    
    time.sleep(3)
    print("After subtracting the values by the average, we square them:")
    print(variSList)
    print(" ")

    variTotal = 0
    for vt in variSList:
        variTotal += vt
    
    time.sleep(3)
    print("Add all those values together, and you get " + str(variTotal) + ".")

    quickQues = ""
    while (True):
        quickQues = input("\nWhat is being represented in this data? Population or sample? ")
        if quickQues.lower() == "sample":
            numOfValues -= 1
            break
        elif (quickQues.lower() != "sample" and quickQues.lower() != "population"):
            continue
    
    vari = variTotal / numOfValues

    time.sleep(3)
    print(" ")
    print("With all the squared values added together, we can now find the variance.\n")
    print(str(variTotal) + " / " + str(numOfValues) + " = " + str(vari) + "\n")

    standardD = vari ** 0.5

    time.sleep(3)
    print("It's time to wrap this whole thing up and find the standard deviation.\n")
    print("The standard deviation is the square root of the variance, so the answer is " + str(standardD) + ".")

    # Median & Range

    while (True):   
        nextOne = input("\nWould you like to find the median and range? (Y/N): ")
        
        if (nextOne.lower() == "y"):
            median = 0
            numOfValues += 1

            time.sleep(3)
            valueList = values
            valueList.sort()
            print("\nFirst, we sort out the list.")
            print(valueList)
            time.sleep(3)
            print("\nNow, to generate the median and range...")
            time.sleep(3)

            if numOfValues % 2 == 0:
                median1 = valueList[(numOfValues//2)-1]
                median2 = valueList[(numOfValues//2)]
                median = (median1 + median2)/2
            else:
                median = valueList[numOfValues//2]
    
            range = valueList[-1] - valueList[0]
    
            print("\nThe median & range of this set of numbers is " + str(median) + " and " + str(range) + ".")
            break

        elif (nextOne.lower() == "n"):
            break

        elif (nextOne.lower() != "y" and nextOne.lower() != "n"):
            continue
    
standardDeviation()