# Author: Anthony Corton
# Date: 8/30/2021
# Description: Practicing leetcode problem #101 the topic being given a tree
# root return True if its a mirror of itself (symmetrical)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.helperSym(root.left, root.right)

    def helperSym(self, p, q):

        if p is None and q is None:
            return True

        elif (p is None or q is None) or (p.val != q.val):
            return False

        return self.helperSym(p.left, q.right) and self.helperSym(
            p.right, q.left)


