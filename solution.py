# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class minList:
    def __init__(self):
        self.l = []
        self.m = 9999999
    
    def __len__(self):
        return len(self.l)

    def __str__(self):
        return str(self.l)
    
    def append(self, n):
        self.l.append(n)
        if len(self.l) >= 2:
            self.m = min(self.m, self.l[len(self.l) - 1] - self.l[len(self.l) - 2])
    
    def getMin(self):
        return self.m

class Solution:
    def inorder(self, root, arr):
        if root is None:
            return
        
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = minList()
        self.inorder(root, arr)
        print(arr)
        return arr.m
