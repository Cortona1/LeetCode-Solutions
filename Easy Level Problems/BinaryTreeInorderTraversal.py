# Author: Anthony Corton
# Date: 8/27/2021
# Description: Practicing leetcode problem #94 the topic being given the root
# of a binary tree return the in order traversal of its nodes value as a list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [
            root.val] + self.inorderTraversal(root.right)