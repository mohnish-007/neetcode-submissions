# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prevGroup=dummy
        while True:
            kth=self.getKth(prevGroup,k)
            if not kth:
                break
            nextGroup=kth.next
            prev,curr=kth.next,prevGroup.next
            while curr!=nextGroup:
                nextNode=curr.next
                curr.next=prev
                prev=curr
                curr=nextNode
            temp=prevGroup.next
            prevGroup.next=kth
            prevGroup=temp

        return dummy.next

    def getKth(self,curr,k):
        while curr is not None and k>0:
            curr=curr.next
            k-=1
        return curr