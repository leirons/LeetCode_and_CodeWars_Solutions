#Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        while head != None:
            cur = head
            head = head.next
            cur.next = previous
            previous = cur
        return previous