# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        return self.num_to_link_list(self.link_list_to_num(l1) + self.link_list_to_num(l2))


    def link_list_to_num(self, root):
        num = root.val
        count = 1
        while root.next != None:
            root = root.next
            num += root.val * (10 ** count)
            count += 1
        return num

    def num_to_link_list(self, num):
        str_num = str(num)
        digit = len(str_num) - 1
        root = ListNode(int(str_num[digit]))
        digit -= 1
        last_node = root
        while digit >= 0:
            new_node = ListNode(int(str_num[digit]))
            last_node.next = new_node
            last_node = new_node
            digit -= 1
        return root


sol = Solution()
l1 = ListNode(5)
l2 = ListNode(5)
print(sol.addTwoNumbers(l1,l2).val)
