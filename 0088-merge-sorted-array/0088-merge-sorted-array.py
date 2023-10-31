class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        nums1.sort(reverse=True)
        for num in nums2:
            if 0 in nums1:
                nums1.remove(0)
            nums1.append(num)
        nums1.sort()

        """
        Do not return anything, modify nums1 in-place instead.
        """
        