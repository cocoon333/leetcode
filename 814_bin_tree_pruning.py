"""
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root):
        res = self.recPruneTree(root)
        if res:
            return root
        return None

    def recPruneTree(self, root):
        if not root:
            return False
        left = self.recPruneTree(root.left)
        right = self.recPruneTree(root.right)

        if not left:
            root.left = None
        if not right:
            root.right = None

        return left or right or root.val
