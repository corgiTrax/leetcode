class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None: return head
    
        cur_node = head 
        while cur_node != None:
            while cur_node.next != None and cur_node.val == cur_node.next.val:
                cur_node.next = cur_node.next.next
                
            cur_node = cur_node.next

        return head
