# Author: Anthony Corton
# Date: 8/28/2021
# Description: Practicing leetcode problem #100 the topic being given two tree
# roots return True if they are structurally identical


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        elif (p is None or q is None) or (p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,
                                                                   q.right)