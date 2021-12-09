# Author: Anthony Corton
# Date: 12/8/2021
# Description: Practicing leetcode problem #2, from Medium List,
# given two non-empty linked list representing two non-negative integers in
# reverse order sum up the numbers as a new linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
    Optional[ListNode]:

        l1_value = self.navigateLinkedList(l1, "")
        l2_value = self.navigateLinkedList(l2, "")

        sum = self.sumLinkedList(l1_value, l2_value)
        node = ListNode()

        sum_node = self.createLinkedList(node, node, sum, len(sum) - 1)

        return sum_node

    def createLinkedList(self, head, node, string, index):

        if index == -1:
            return head  # return za head at the end!

        if index == len(string) - 1:  # beginning of function call
            node.val = string[index]
            head = node  # to prevent returning last node keep track of the head (python != pointers)
            return self.createLinkedList(head, node, string, index - 1)

        else:
            new_node = ListNode()
            new_node.val = string[index]
            new_node.next = None
            node.next = new_node  # assign new node to the end of the current node

            return self.createLinkedList(head, new_node, string, index - 1)

    def sumLinkedList(self, x, y):
        return str(int(x) + int(y))

    def navigateLinkedList(self, node, stringValue):
        if node.next == None:
            return str(node.val) + stringValue

        else:
            return self.navigateLinkedList(node.next,
                                           str(node.val) + stringValue)