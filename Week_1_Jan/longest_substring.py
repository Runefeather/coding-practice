# Question #: 9
# Date: Jan 2 2021
# Author: Dhanya
# Leetcode Challenge week 1

# PROMPT
# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 0):
            return 0

        if(len(''.join(set(s))) == 1):
            return 1 

        maxsub = 1
        i = 0
        while i < len(s):
            sub = ''
            visited = {}
            for j in range(i, len(s)):
                if(s[j] not in visited):
                    visited[s[j]] = 1
                    sub = sub + s[j]
                else:
                    break
            if(len(sub) > maxsub):
                maxsub = len(sub)

            if(i > len(s)/2 and maxsub > len(s)/2):
                break

            i += 1

        return maxsub
        
if __name__ == "__main__":
    prob1 = Solution()
    print(prob1.lengthOfLongestSubstring("dvdf"))
