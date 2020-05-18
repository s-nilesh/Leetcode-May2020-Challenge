#PROBLEM
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

#SOLUTION-1
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        l = len(s1)
        for i in range(len(s2)):
            if counts[s2[i]] > 0:
                l -= 1
            counts[s2[i]] -= 1
            if l == 0:
                return True
            start = i + 1 - len(s1)
            if start >= 0:
                counts[s2[start]] += 1
                if counts[s2[start]] > 0:
                    l += 1
        return False
        

#SOLUTION-2  
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1h=0
        s2h=0
        if len(s2)<len(s1):
            return False
        for i in s1:
            s1h+=hash(i)
        for i in range(len(s1)):
            s2h+=hash(s2[i])
        if s1h==s2h:
            return True
        if len(s2)>len(s1):
            for j in range(len(s1),len(s2)):
                s2h+=hash(s2[j])-hash(s2[j-len(s1)])
                if s1h==s2h:
                    return True
        return False


#SOLUTION-3
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=""
        for i in range(0,len(s2)-len(s1)+1):
            m=s2[i:i+len(s1)]
            if Counter(m)==Counter(s1):
                return True
        return False