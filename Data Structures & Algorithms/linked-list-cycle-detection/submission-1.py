# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we use two pointers that move a different speeds so if it is ever lapped there is a cycle
        slow, fast = head, head

        # move through the list in one and two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # If at any point slow == fast, a cycle exists, return true.
            if slow == fast:
                return True
        return False
        