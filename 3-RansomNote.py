#PROBLEM
#Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

#Each letter in the magazine string can only be used once in your ransom note.

#Note:
#You may assume that both strings contain only lowercase letters.

#canConstruct("a", "b") -> false
#canConstruct("aa", "ab") -> false
#canConstruct("aa", "aab") -> true






#SOLUTION-1
from collections import Counter
class Solution:
    # def return_dict(self, string: str) -> dict:
    #     str_d = {}
    #     for letter in string:
    #         if letter in str_d:
    #             str_d[letter] += 1
    #         else:
    #             str_d[letter] = 1
    #     return str_d
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # flag = True
        # rn_dict = self.return_dict(ransomNote)
        # mag_dict = self.return_dict(magazine)
        # for rn_letter in rn_dict.keys():
        #     if ((rn_letter not in mag_dict.keys()) or (mag_dict[rn_letter] < rn_dict[rn_letter])):
        #         flag = False
        #         break
        #     else:
        #         flag = True

        return Counter(ransomNote) - Counter(magazine) == {}

#SOLUTION-2
class Solution:
    def return_dict(self, string: str) -> dict:
        str_d = {}
        for letter in string:
            if letter in str_d:
                str_d[letter] += 1
            else:
                str_d[letter] = 1
        return str_d
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        flag = True
        rn_dict = self.return_dict(ransomNote)
        mag_dict = self.return_dict(magazine)
        for rn_letter in rn_dict.keys():
            if ((rn_letter not in mag_dict.keys()) or (mag_dict[rn_letter] < rn_dict[rn_letter])):
                flag = False
                break
            else:
                flag = True
    return flag
