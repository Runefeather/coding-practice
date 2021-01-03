# Question #: 7
# Date: Jan 2 2021
# Author: Dhanya
# Leetcode Challenge week 1

# PROMPT
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# My solution
class Solution:
    def twoSum(self, nums, target):
        
        if(len(nums) == 2):
            return([0,1])
        
        sub = {(target - nums[i]):i for i in range(len(nums))}
        
        for n in range(len(nums)):
            if nums[n] in sub and n != sub[nums[n]] :
                return([n, sub[nums[n]]])

# Fastest solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         h = {}
#         for i in range(len(nums)):
#             rem = target - nums[i]
#             if rem in h:
#                 return([i, h[rem]])
#             else:
#                 h[nums[i]] = i
                

if __name__ == "__main__":
    prob1 = Solution()
    print(prob1.twoSum([3,4,2], 6))
