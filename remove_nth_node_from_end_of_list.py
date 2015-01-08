# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''An O(n) solution without extra space'''
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        #maintain 3 pointers, move them consecutively
        target = head
        parent_target = head
        cur_node = head

        count = 0
        while cur_node:
            if count >= n:
                target = target.next
            if count > n:
                parent_target = parent_target.next

            if cur_node.next == None:
                if not(parent_target is target):
                    parent_target.next = target.next                
                    return head
                else:
                    return head.next

            count += 1
            cur_node = cur_node.next
        



         
