# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

low = float('-inf')
high = float('inf')

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.Validator(root,low,high)

    def Validator(self,root,low,high):
        if root is None:
            return True
        if low < root.val < high :
            if self.Validator(root.left,low,root.val) and self.Validator(root.right,root.val,high):
                return True
            else:
                return False
        else:
            return False
        
