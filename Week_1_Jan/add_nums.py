# Question #: 8
# Date: Jan 2 2021
# Author: Dhanya
# Leetcode Challenge week 1

# PROMPT
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# My solution
class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_over = 0
        sum = []
        x = 0
        y = 0
        while x < len(l1) or y < len(l2):
            if x >= len(l1):
                l1.append(0)
            elif(y >= len(l2)):
                l2.append(0)
            sum.append((l1[x] + l2[y] + carry_over)%10)
            if(l1[x] + l2[y] + carry_over > 10):
                carry_over = l1[x] + l2[y] + carry_over - 10
            else:
                carry_over = 0
            x += 1
            y += 1
        
        return sum
        

if __name__ == "__main__":
    prob1 = Solution()
    print(prob1.addTwoNumbers([3,4,2], [6]))
