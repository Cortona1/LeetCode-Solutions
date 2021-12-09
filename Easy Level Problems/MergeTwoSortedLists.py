# Author: Anthony Corton
# Date: 8/18/2021
# Description: Practicing leetcode problem #21 the topic being merge two
# sorted linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next


        if l1:
            tail.next = l1

        elif l2:
            tail.next = l2

        return dummy.next





l3 = ListNode()
l3.val = 1

num_2 = ListNode()
num_2.val = 2

num_4 = ListNode()
num_4.val = 4

l3.next = num_2
num_2.next = num_4

l4 = ListNode()
l4.val = 3
num_5 = ListNode()
num_5.val = 5

l4.next = num_5


#count = l3
#while (count):
    #print(count.val)
    #count = count.next

test = Solution()
answer = test.mergeTwoLists(l3, l4)

while (answer):
    print(answer.val)
    answer = answer.next