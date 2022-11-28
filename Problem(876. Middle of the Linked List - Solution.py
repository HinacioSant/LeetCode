# Problem 876. Middle of the Linked List:

#  Given the head of a singly linked list, return the middle node of the
# linked list.  If there are two middle nodes, return the second
# middle node.

# Solution:
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head
        while a and a.next:
            b = b.next
            a = a.next.next
        return b
