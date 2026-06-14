import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    randomGenerator = random.random()

    dateFormat = "%m/%d/%Y"
    # strptime = parsing or rearranging date format from yyyy-mm-dd to m/d/yyy 
    # and then mktime = reformatting into package with 9 elements
    starttime = time.mktime(time.strptime(startDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))

    # localtime is reformatting from float number into package with 9 elements,
    # strftime reformatting from package into dateformat
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    
    return randomDate

result = getRandomDate("4/23/2025", "12/31/2025")
print("Random Date = ", result)