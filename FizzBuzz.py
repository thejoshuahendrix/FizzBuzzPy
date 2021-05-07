
for i in range(1,101):
    logString = ""
    if i % 3 == 0:
        logString += "Fizz"
    if i % 5 == 0:
        logString += "Buzz"
    if logString == "":
        print(i)
    else:
        print(logString)
        
        
