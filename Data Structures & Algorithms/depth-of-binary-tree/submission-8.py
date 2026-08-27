# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## ITERATIVE DFS ##
## DFS USES?? ##
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack=[[root,1]]
        res=0
        while stack:
            a,depth = stack.pop()
            if a:
                res=max(res,depth)
                stack.append([a.left,depth+1])
                stack.append([a.right,depth+1])
        return res
