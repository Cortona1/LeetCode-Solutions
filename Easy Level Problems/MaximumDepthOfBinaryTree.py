# Author: Anthony Corton
# Date: 8/30/2021
# Description: Practicing leetcode problem #104 the topic being given a binary
# tree return its maximum depth


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # edge cases

        if root is None:
            return 0

        test_l = self.nodeSearch(root.left, 1)

        test_r = self.nodeSearch(root.right, 1)

        return max(test_l, test_r)

    def nodeSearch(self, root, counter):

        if root is None:
            return counter

        else:
            counter += 1
            return max(self.nodeSearch(root.left, counter),
                       self.nodeSearch(root.right, counter))
