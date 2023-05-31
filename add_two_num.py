# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        a = [str(i) for i in l1]
        b = [str(i) for i in l2]

        res = str(int("".join(a)) + int("".join(b)))[::-1]
        return list(res)


print(Solution.addTwoNumbers([2, 4, 3], [5, 6, 4]))
