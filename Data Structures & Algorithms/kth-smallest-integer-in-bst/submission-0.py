# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ''' i should use DFS because the smallest element would b in the left bottom most leaf'''
        stack=[]
        curr=root
        ctr=0
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            ctr+=1
            if ctr==k:
                return curr.val
            curr=curr.right