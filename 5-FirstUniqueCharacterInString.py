#PROBLEM
#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

#Examples:

#s = "leetcode"
#return 0.

#s = "loveleetcode",
#return 2.

#Note: You may assume the string contain only lowercase letters.




#SOLUTION
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_count = Counter(s)
        req_letter_index = -1
        for letter,rep in letter_count.items(): 
            if rep == 1: 
                req_letter_index = s.index(letter) 
                break
            else:
                req_letter_index = -1
        return req_letter_index
