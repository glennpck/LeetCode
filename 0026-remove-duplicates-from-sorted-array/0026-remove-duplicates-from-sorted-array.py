class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        const = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[const] = nums[i]
                const += 1
                    
        return const