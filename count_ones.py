# Question #: 2
# Date: Jan 1 2021
# Author: Dhanya

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    # Get the input array
    # Get length of array
    N = int(input())
    arr = []
    count = 0
    # get elements of array
    for i in range(N):
        arr.append(int(input()))
        if arr[-1] == 1:
            count += 1
    
    print(count)
    return count

main()

