# Question #: 6
# Date: Jan 2 2021
# Author: Dhanya
# Leetcode Challenge week 1
import itertools

# # PROMPT
# Given two binary trees original and cloned and given a reference to a node target in the original tree.
# The cloned tree is a copy of the original tree.
# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

# Follow up: Solve the problem if repeated values on the tree are allowed.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        old_cloned = []
        
        while True:
            if(cloned.val == target.val):
                return cloned
            else:
                if(cloned.left is not None):
                    if(cloned.right is not None):
                        old_cloned.append(cloned.right)
                    cloned = cloned.left
                elif(cloned.right is not None):
                    cloned = cloned.right
                else:
                    cloned = old_cloned[-1]
                    old_cloned.pop(-1)
            
            

    