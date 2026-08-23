
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we create a dummy node and a node pointer to it
        dummy = node = ListNode()

        # While both the lists have nodes
        while list1 and list2:
            # Compare list1.val and list2.val.
            if list1.val < list2.val:
                # Attach the smaller node to node.next.
                node.next = list1
                # Move forward in the chosen list.
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
            
        # Attach the remaining nodes of the other list to node.next.
        node.next = list1 or list2

        return dummy.next


        