#PROBLEM

#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#You may assume that the array is non-empty and the majority element always exist in the array.

#Example 1:
#Input: [3,2,3]
#Output: 3

#Example 2:
#Input: [2,2,1,1,1,2,2]
#Output: 2


#SOLUTION-1
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = Counter(nums)
        return list(dic.keys())[list(dic.values()).index(max(dic.values()))]

#SOLUTION-2 (beats 99.99% of other solutions)
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = Counter(nums)
        return sorted(dic, key=dic.get, reverse=True)[0]


