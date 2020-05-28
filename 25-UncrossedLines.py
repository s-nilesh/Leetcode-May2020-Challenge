#PROBLEM
# We write the integers of A and B (in the order they are given) on two separate horizontal lines.

# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

# A[i] == B[j];
# The line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

# Return the maximum number of connecting lines we can draw in this way.

# Example 1:
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2

# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

# Example 2:
# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3

# Example 3:
# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2
 
# Note:
# 1 <= A.length <= 500
# 1 <= B.length <= 500
# 1 <= A[i], B[i] <= 2000



#SOLUTION-1
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        nums = set(A) & set(B)
        A, B = [i for i in A if i in nums], [i for i in B if i in nums]
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]

#SOLUTION-2
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if len(A) < len(B):
            return self.maxUncrossedLines(B, A)

        dp = [[0 for _ in range(len(B)+1)] for _ in range(2)]
        for i in range(len(A)):
            for j in range(len(B)):
                dp[(i+1)%2][j+1] = max(dp[i%2][j] + int(A[i] == B[j]),
                                       dp[i%2][j+1],
                                       dp[(i+1)%2][j])
        return dp[len(A)%2][len(B)]