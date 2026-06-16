class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = len(nums1)

        while low <= high:
            i = low + (high - low) // 2
            j = (len(nums1) + len(nums2) + 1) // 2 - i

            a_left = nums1[i - 1] if i > 0 else float("-inf")
            a_right = nums1[i] if i < len(nums1) else float("inf")

            b_left = nums2[j - 1] if j > 0 else float("-inf")
            b_right = nums2[j] if j < len(nums2) else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
                else:
                    return max(a_left, b_left)
            elif a_left > b_right:
                high = i - 1
            else:
                low = i + 1
        return 0.0