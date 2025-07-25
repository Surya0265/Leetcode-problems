# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        apoint=list1
        bpoint=list1
        for i in range(a-1):
            apoint=apoint.next
        for i in range(b):
            bpoint=bpoint.next
        apoint.next=list2
        while list2.next:
            list2=list2.next
        list2.next=bpoint.next
        return list1
        
        