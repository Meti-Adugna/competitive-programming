class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        output = 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                u = nums[i - 1] + 1
                output += u - nums[i]
                nums[i] = u
        return output
