#PROBLEM:
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

# Follow up: Your solution should run in O(log n) time and O(1) space.

# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 
# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5

#SOLUTION-1
from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return list(counter.keys())[list(counter.values()).index(1)]
    
    
#SOLUTION-2
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0,len(nums),2):
            if len(nums)-i == 1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]
            
        
#SOLUTION-3 (BEST)
class Solution:
    def find(self, nums, left, right): 
        if left > right: 
            return None

        if left == right: 
            return nums[left] 

        mid = left + (right - left)//2

        if mid%2 == 0: 

            if nums[mid] == nums[mid+1]: 
                return self.find(nums, mid+2, right) 
            else: 
                return self.find(nums, left, mid) 

        else: 
            if nums[mid] == nums[mid-1]: 
                return self.find(nums, mid+1, right) 
            else: 
                return self.find(nums, left, mid-1) 
            
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return self.find(nums, 0, len(nums)-1)



        