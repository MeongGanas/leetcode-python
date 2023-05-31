class Solution(object):
    def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        list1.extend(list2)
        list1.sort()

        return list1


print(Solution.mergeTwoLists([1, 2, 4], [1, 3, 4]))
