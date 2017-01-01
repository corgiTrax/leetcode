# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rabbit = turtle = head
        while rabbit and not(rabbit.next == None or rabbit.next.next == None):
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit: return True
        return False
