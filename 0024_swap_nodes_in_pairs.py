# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        foo = ListNode(0)
        foo.next = head
        cur = foo
        while cur.next and cur.next.next:
            second = cur.next
            third = cur.next.next
            cur.next = third
            second.next = third.next
            third.next = second
            cur = cur.next.next
        return foo.next

a = [1,2,3,4]
items = []
for val in a:
    item = ListNode(val)
    items.append(item)
for i in range(len(items) - 1):
    items[i].next = items[i + 1]

sol = Solution()
head = sol.swapPairs(items[0])

while head != None:
    print(head.val)
    head = head.next
