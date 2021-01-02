# Question #: 5
# Date: Jan 1 2021
# Author: Dhanya
# Leetcode Challenge week 1
import itertools

# PROMPT
# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

class Solution(object):

    def contains_sublist(self, lst, sublst):
        n = len(sublst)
        return any((sublst == lst[i:i+n]) for i in range(len(lst)-n+1))

    def canFormArray(self, arr, pieces):
        if(len(pieces) == 1):
            return arr == pieces[0]
        r = len(pieces)
        combis = list(itertools.combinations(pieces, r))
        combis = sum([[list(i) for i in x] for x in combis], [])
        retval = []
        for i in combis:
            retval.append(self.contains_sublist(arr, i))

        return all(r == True for r in retval)


if __name__ == "__main__":
    prob1 = Solution()

    # Input: arr = [85], pieces = [[85]]
    print(prob1.canFormArray([85], [[85]]))

    # Input: arr = [15,88], pieces = [[88],[15]]
    print(prob1.canFormArray([15,88], [[88],[15]]))

    # Input: arr = [49,18,16], pieces = [[16,18,49]]
    print(prob1.canFormArray([49,18,16], [[16,18,49]]))

    # Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
    print(prob1.canFormArray([91,4,64,78], [[78],[4,64],[91]]))

    # Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
    print(prob1.canFormArray([1,3,5,7], [[2,4,6,8]]))

    print(prob1.canFormArray([1,3,2,4,5,6], [[1,2],[3,4],[5,6]]))


    