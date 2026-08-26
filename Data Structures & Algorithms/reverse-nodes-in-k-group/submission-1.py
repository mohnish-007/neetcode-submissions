# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevNGroup=dummy=ListNode(0,head)
        while True:
            kth=prevNGroup
            for _ in range(k):
                kth=kth.next
                if not kth:
                    return dummy.next
            nextNGroup=kth.next
            prev,curr=nextNGroup, prevNGroup.next
            while curr!=nextNGroup:
                nextNode=curr.next
                curr.next=prev
                prev=curr
                curr=nextNode
            temp=prevNGroup.next
            prevNGroup.next=kth
            prevNGroup=temp
        return dummy.next
            