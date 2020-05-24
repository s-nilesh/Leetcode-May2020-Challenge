#PROBLEM
# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

# Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

 

# Constraints:

# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# The values of preorder are distinct.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#SOLUTION-1
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(high=inf):
            if not (preorder and preorder[0] < high):
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            root.left = helper(val)
            root.right = helper(high)
            return root
        return helper()


#SOLUTION-2
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def bstFromPreorderHelper(preorder, left, right, index):
            if index[0] == len(preorder) or \
               preorder[index[0]] < left or \
               preorder[index[0]] > right:
                return None

            root = TreeNode(preorder[index[0]])
            index[0] += 1
            root.left = bstFromPreorderHelper(preorder, left, root.val, index)
            root.right = bstFromPreorderHelper(preorder, root.val, right, index)
            return root
        
        return bstFromPreorderHelper(preorder, float("-inf"), float("inf"), [0])