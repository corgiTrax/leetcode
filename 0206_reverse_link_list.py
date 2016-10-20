# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        pre = None
        cur = head
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        return pre

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head, None)
        
    def reverse(self, head, pre):
        if not head: return pre
        temp = head.next 
        head.next = pre
        pre = temp
        return self.reverse(pre, head)
