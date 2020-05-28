#PROBLEM
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into the same group. 

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.

# Example 1:
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]

# Example 2:
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false

# Example 3:
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
 
# Note:
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].




#SOLUTION_1
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(N)]
        for u, v in dislikes:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)

        color = [0]*N
        color[0] = 1
        q = collections.deque([0])
        while q:
            cur = q.popleft()
            for nei in adj[cur]:
                if color[nei] == color[cur]:
                    return False
                elif color[nei] == -color[cur]:
                    continue
                color[nei] = -color[cur]
                q.append(nei)
        return True
    
    
#SOLUTION-2
from collections import defaultdict
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        edges = defaultdict(list)
        for d in dislikes:
            edges[d[0]].append(d[1])
            edges[d[1]].append(d[0])
        group = [0]*(N+1)
        for i in range(1, N+1):
            if group[i]==0 and (i in edges) and not self.dfs(i, edges, group, 1):
                return False
        return True

    def dfs(self, i, edges, group, g):
        """whether it is possible to put i in group g"""
        group[i] = g
        for neighbor in edges[i]:
            if group[neighbor] == group[i]:
                return False
            if group[neighbor]==0 and not self.dfs(neighbor, edges, group, -1*g): 
                return False
        return True