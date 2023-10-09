import functools


class Solution(object):
    def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) > 1 and len(nums1) % 2 == 1:
            return float(nums1[int(len(nums1)/2)])
        else:
            return (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2)-1])/2.0


print(Solution.findMedianSortedArrays([1, 3], [2]))
