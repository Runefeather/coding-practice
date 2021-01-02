# Question #: 1
# Date: Jan 1 2021
# Author: Dhanya

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

monthDict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def main():
    # Inputs - m, d - month, weekday
    month = int(input())
    day = int(input())
    if(month >= 1 and month <= 12 and day >= 1 and day <= 7): 
        # Get the number of days
        numDays = monthDict[month]
        # Get the leftover days after subtracting the first week
        leftover = numDays - (7 - (day - 1))
        # if divisible by 7
        if(leftover % 7 == 0):
            cols = 1 + int(leftover / 7)
        # if not
        else:
            cols = 1 + int(leftover / 7) + 1

        print(cols)
        return cols

main()

