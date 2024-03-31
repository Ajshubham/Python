# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1 + nums2
        temp.sort()
        if len(temp) % 2 == 0:
            mid = len(temp) // 2
            s = temp[mid-1] + temp[mid]
            return s / 2
        else:
            return temp[len(temp) // 2]
