#Problem
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".




#SOLUTION-1
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        output = []
        p_count = Counter(p)
        for i in range(len(s)-len(p)+1):
            if s[i] not in p:
                continue
            if Counter(s[i:i+lp]) == p_count:
                output.append(i)
        return output

#SOLUTION-2
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        output = []
        p_sort = sorted(p)
        for i in range(len(s)-len(p)+1):
            if s[i] not in p:
                continue
            if sorted(s[i:i+lp]) == p_sort:
                output.append(i)
        return output

#SOLUTION-3
class Solution(object):
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []

        cnts = [0] * 26
        for c in p:
            cnts[ord(c) - ord('a')] += 1

        left, right = 0, 0
        while right < len(s):
            cnts[ord(s[right]) - ord('a')] -= 1
            while left <= right and cnts[ord(s[right]) - ord('a')] < 0:
                cnts[ord(s[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
            right += 1

        return result

#SOLUTION-4
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        hash_p = sum(hash(ch) for ch in p)
        hash_i = sum(hash(ch) for ch in s[:len(p)-1])
        
        ret = []
        for idx, (ch_out, ch_in) in enumerate(zip([""] + list(s), s[len(p)-1:])):
            hash_i += hash(ch_in) - hash(ch_out)
            if hash_i == hash_p:
                ret.append(idx)
                
        return ret