#PROBLEM
#In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

#Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

#We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

#Return true if and only if the nodes corresponding to the values x and y are cousins.

#Example 1:
#Input: root = [1,2,3,4], x = 4, y = 3
#Output: false

#Example 2:
#Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
#Output: true

#Example 3:
#Input: root = [1,2,3,null,4], x = 2, y = 3
#Output: false
 

#Note:
#The number of nodes in the tree will be between 2 and 100.
#Each node has a unique integer value from 1 to 100.


#SOLUTION-1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, a: int, b: int) -> bool:
        if root == None: 
            return False 

        # To store parent of node a.  
        parA = None 

        # To store parent of node b.  
        parB = None 

        # queue to perform level order  
        # traversal. Each element of queue  
        # is a pair of node and its parent.  
        q = []  

        # Dummy node to act like  
        # parent of root node.  
        tmp = TreeNode(-1)  

        # Push root to queue.  
        q.append((root, tmp))  

        while len(q) > 0:   

            # find number of elements in  
            # current level.  
            levSize = len(q)  
            while levSize:   

                ele = q.pop(0)  

                # check if current node is  
                # node a or node b or not.  
                if ele[0].val == a:   
                    parA = ele[1]  

                if ele[0].val == b:   
                    parB = ele[1]  

                # push children of  
                # current node to queue.  
                if ele[0].left:   
                    q.append((ele[0].left, ele[0]))  

                if ele[0].right:   
                    q.append((ele[0].right, ele[0]))  
                levSize -= 1

                # If both nodes are found in  
                # current level then no need  
                # to traverse current level further.  
                if parA and parB:  
                    break 

            # Check if both nodes  
            # are siblings or not.  
            if parA and parB:   
                return parA != parB  

            # If one node is found in current level  
            # and another is not found, then  
            # both nodes are not cousins.  
            if (parA and not parB) or (parB and not parA):  
                return False 

        return False 


#SOLUTION-2
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSibling(self,root, a , b): 
  
        # Base Case 
        if root is None: 
            return 0

        return ((root.left == a and root.right ==b) or 
                (root.left == b and root.right == a)or
                self.isSibling(root.left, a, b) or
                self.isSibling(root.right, a, b)) 

    # Recursive function to find level of Node 'ptr' in  
    # a binary tree 
    def level(self,root, ptr, lev): 

        # Base Case  
        if root is None : 
            return 0 
        if root.val == ptr:  
            return lev 

        # Return level if Node is present in left subtree 
        l = self.level(root.left, ptr, lev+1) 
        if l != 0: 
            return l 

        # Else search in right subtree 
        return self.level(root.right, ptr, lev+1) 
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if ((self.level(root,x,1) == self.level(root, y, 1)) and 
            not (self.isSibling(root, x, y))): 
            return True
        else: 
            return False
