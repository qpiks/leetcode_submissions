class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        ans = float('inf')
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            while (s >= target):
                ans = min(ans, i - l + 1)
                s -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0
        