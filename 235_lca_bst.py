"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.recursivelowestCommonAncestor(root, p.val, q.val)

    def recursivelowestCommonAncestor(self, root, p, q):
        if not(root):
            return

        if root.val == p or root.val == q:
            return root

        p, q = sorted((p, q))
        if p < root.val < q:
            return root

        left = None

        left = self.recursivelowestCommonAncestor(root.left, p, q)
        if left:
            return left
        right = None

        return self.recursivelowestCommonAncestor(root.right, p, q)
