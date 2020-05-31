#PROBLEM
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')



#SOLUTIONS
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i<0 or j<0: return max(i,j)+1
            return dp(i-1,j-1) if s1[i]==s2[j] else min(dp(i-1,j),dp(i-1,j-1),dp(i,j-1))+1
        return dp(len(s1)-1,len(s2)-1)



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        visited = set()
        q = deque([(word1, word2, 0)])
        
        while q:
            w1, w2, dist = q.popleft()
            
            if (w1, w2) not in visited:
                visited.add((w1, w2))

                if w1 == w2:
                    return dist

                while w1 and w2 and w1[0] == w2[0]:
                    w1 = w1[1:]
                    w2 = w2[1:]

                dist += 1
                q.extend([(
                    w1[1:], w2[1:], dist), 
                    (w1, w2[1:], dist), 
                    (w1[1:], w2, dist)])