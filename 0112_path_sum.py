# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        elif root.left != None and root.right != None:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        elif root.left == None and root.right == None:
            if sum == root.val: return True
            else: return False 
        elif root.left == None:
            return self.hasPathSum(root.right, sum - root.val)
        elif root.right == None:
            return self.hasPathSum(root.left, sum - root.val)
        
        
