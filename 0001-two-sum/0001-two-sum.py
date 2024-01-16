class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in nums:
            search = target - i
            if search in nums and search != i:
                ans.append(nums.index(i))
                ans.append(nums.index(search))
                break
            elif search in nums and nums.count(search) > 1:
                ans.append(nums.index(i))
                nums[nums.index(i)] = i+1
                ans.append(nums.index(search))
                break
                
        return ans
                