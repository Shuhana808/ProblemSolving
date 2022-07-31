class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        window_sum = 0
        min_length = 100001
        start = 0
        end = 0

        for i in range(0, n):
            window_sum = window_sum + nums[i]

            while window_sum >= target:
                min_length = min(min_length, i - start + 1)

                window_sum = window_sum - nums[start]
                start = start + 1

        if min_length == 100001:
            min_length = 0

        return min_length
