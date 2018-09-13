# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        onestep = twostep = head
        while True:
            if twostep.next == None:
                return onestep
            elif twostep.next.next == None:
                return onestep.next
            else:
			    onestep = onestep.next
			    twostep = twostep.next.next
        return onestep