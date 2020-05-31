#PROBLEM
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
 

# Constraints:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5


#SOLUTIONS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        deg = [0]*numCourses
        
        for i, j in prerequisites:
            graph[j].append(i)
            deg[i] += 1
        
        queue = collections.deque([i for i, v in enumerate(deg) if v==0])
        
        while queue:
            cur_v = queue.popleft()
            for neighbor in graph[cur_v]:
                deg[neighbor] -= 1
                if deg[neighbor]==0:
                    queue.append(neighbor)
 
        return not sum(deg)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        def dfs(adj, u):
            exploring[u] = True
            
            for n in adj[u]:
                if finished[n] == True:
                    continue
                if exploring[n] == True:
                    self.cycle = True
                    return
                dfs(adj, n)
            
            finished[u] = True
        
        
        def hasCycle(adj):
            
            for idx in range(numCourses):
                dfs(adj, idx)
            return self.cycle
        
        
        self.cycle = False
        adj = [[] for _ in range(numCourses)]
        exploring = [False] * numCourses
        finished = [False] * numCourses
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
            
        if hasCycle(adj) == True:
            return False
        
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]

        for x, y in prerequisites:
            graph[x].append(y)

        for i in range(numCourses):
            if not self.dfs(i, visit, graph):
                return False

        return True

    def dfs(self, i, visit, graph):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True

        visit[i] = -1
        for j in graph[i]:
            if not self.dfs(j, visit, graph):
                return False
        visit[i] = 1

        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for i in range(numCourses)] 
        connection = {i:[] for i in range(numCourses)}
        for link in prerequisites:
            connection[link[1]].append(link[0])
            indegree[link[0]] += 1
        zero_indegree = []
        for i in range(numCourses):
            if indegree[i] == 0:
                zero_indegree.append(i)
        i = 0
        while i<len(zero_indegree):
            for node in connection[zero_indegree[i]]:
                indegree[node] -= 1
                if  indegree[node] == 0:
                    zero_indegree.append(node)
            i += 1
        if len(zero_indegree) == numCourses:
            return True
        else:
            return False        

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = [[0 for i in range(numCourses)] for j in range(numCourses)]
        for s in prerequisites:
            course[s[0]][s[1]] = 1
            
        visited = [0 for i in range(numCourses)]
        for i in range(numCourses):
            if self.dfs(course, i, visited)==False:
                return False
        return True
                
        
    def dfs(self, course, num, visited):
        for i in range(len(course[num])):
            if course[num][i] == 1:
                visited[num] = 1
                if visited[i] == 1:
                    return False
                else:
                    if self.dfs(course, i, visited) == False:
                        return False
                    visited[num] = 0