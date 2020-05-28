#PROBLEM
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Note: The length of the given binary array will not exceed 50,000.



#SOLUTION-1
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result, count = 0, 0
        lookup = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in lookup:
                result = max(result, i - lookup[count])
            else:
                lookup[count] = i
        
        return result


#SOLUTION-2
from collections import Counter
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        max_len = 0
        counter = Counter(nums)
        max_possible_len = (counter[min(counter)]*2)
        for i in range(len(nums)-1):
        #     if max_len >= (counter[min(counter)]*2):
        #         break
            j = i+1
            while j<len(nums) and (max_len < max_possible_len):   
        #     for j in range(i+1,len(nums)):
                # print(nums[i:j+1])
                count = Counter(nums[i:j+1])
                if (count[0] == count[1]) and (len(nums[i:j+1])>max_len):
                    max_len = len(nums[i:j+1])
                j += 1
        return max_len