# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean

    def isSameTree(self, p, q):
        #recursive solution
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else: #both are not none
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean

    def isSameTree(self, p, q):
        #traverse solution
        if p == None and q == None: return True
        p_list, q_list = [], []
        self.traverse(p, p_list)
        self.traverse(q, q_list)
        if p_list == q_list:
            return True
        else:
            return False
        
    def traverse(self, root, tree_list):
        #perform an in order traverse of the tree and returns a list
        if root == None:
            pass
        else:
            tree_list.append(root.val)
            if root.left == None:
                tree_list.append('#')
            else:    
                self.traverse(root.left, tree_list)
            if root.right == None:
                tree_list.append('#')
            else:
                self.traverse(root.right, tree_list)
        
'''Note: traverse solution is very tricky
consider tree {10,5,15} and tree {10,5,#,#,15},
the normal traversed array will give you [10,5,15] for both
so we need also to record empty children by #'''    
        
