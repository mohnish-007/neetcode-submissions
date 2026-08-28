# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy 

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode
                             ) -> TreeNode:
        #get ancestors
        l1 = self.getAncestors(root, p, [])
        l2 = self.getAncestors(root, q, [])

        #invert lists
        #l1 = l1[::-1]
        #l2 = l2[::-1]

        for node in l1:
            print(node.val)
        print("Checking")
        for node in l2:
            print(node.val)

        #find until they dont match
        matchNode = root
        for iterLin in range(1,min(len(l1), len(l2))):
            if l1[iterLin].val == l2[iterLin].val:
                matchNode = l1[iterLin]

        return matchNode

    def getAncestors(self, 
                     root: TreeNode, 
                     searchNode: TreeNode, ancestorList: list) -> list: 
        if root == None:
            return None

        ancestorList.append(root)

        if root == searchNode: 
            return ancestorList

        l1 = self.getAncestors(root.left, searchNode, copy.deepcopy(ancestorList))
        l2 = self.getAncestors(root.right, searchNode, copy.deepcopy(ancestorList))
        
        if l1:
            return l1
        if l2:
            return l2 
        