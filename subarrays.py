# Question #: 4
# Date: Jan 1 2021
# Author: Dhanya
from functools import reduce
import itertools
from operator import xor

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    # get k, n
    k = int(input())
    arr = []
    total = 0
    for i in range(int(input())):
        arr.append(int(input()))

    for r in range(len(arr)):
        combi = [arr[i : i+r+1] for i in range(len(arr) - r)]
        for item in combi:
            res = reduce(xor, map(int, item))
            if (res >= k):
                total += 1
    
    print(total)
    return total


main()

