#PROBLEM
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones. 

# Example 1:
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

# Example 2:
# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
 
# Constraints:
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1



#SOLUTION-1
import numpy as np
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0
        for side in range(1,min(arr.shape)+1):
            sub_arr_sum = side**2
            for i in range(arr.shape[0]-side+1):
                for j in range(arr.shape[1]-side+1):
                    if arr[i,j]:
                        if np.sum(arr[i:i+side,j:j+side]) == sub_arr_sum:
                            result += 1
        return result



#SOLUTION-2
import numpy as np
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        arr = np.array(matrix)
        return np.sum([1 for side in range(1,min(arr.shape)+1) for i in range(arr.shape[0]-side+1) for j in range(arr.shape[1]-side+1) if arr[i,j] and (sum(sum(arr[i:i+side,j:j+side])) == side**2)])

        

#SOLUTION-3
import numpy as np
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        arr = np.array(matrix)
        result = 0
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                if arr[i,j]:
                    for side in range(1,min(arr.shape[0]-i, arr.shape[1]-j)+1):
                        if np.sum(arr[i:i+side,j:j+side]) == side**2:
                            result += 1
        return result

        

#SOLUTION-4
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][j]:
                    continue
                l = min(matrix[i-1][j], matrix[i][j-1])
                matrix[i][j] = l+1 if matrix[i-l][j-l] else l
        return sum(x for row in matrix for x in row)