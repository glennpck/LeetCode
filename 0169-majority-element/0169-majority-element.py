class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        most_common = counter.most_common(1)
        return most_common[0][0]
        