# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.psyduck(root.left,root.right)
    
    def psyduck(self,leftroot,rightroot):
        if leftroot and rightroot:
            return leftroot.val == rightroot.val and self.psyduck(leftroot.left,rightroot.right) and self.psyduck(rightroot.left,leftroot.right)
        return leftroot == rightroot
        
