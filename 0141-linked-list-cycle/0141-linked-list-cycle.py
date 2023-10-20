'''
Cesar Emilio Castaño Marin
Solution: Linked List Cycle
Github Username: CesarEmilioC
Technique: Use two pointers and check if they meet at some point, or the list has an end.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        fast_pointer = head.next
        slow_pointer = head
        while fast_pointer != slow_pointer:
            try:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            except:
                return False
        return True

        