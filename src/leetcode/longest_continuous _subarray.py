from typing import List
import heapq as hq
from icecream import ic


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []
        start = 0
        max_subarray_len = 0
        for i in range(len(nums)):
            ic(i)
            hq.heappush(max_heap, (-1*nums[i], i))
            hq.heappush(min_heap, (nums[i], i))
            while len(max_heap)>0:
                mx, max_index = max_heap[0]
                mx = -1*mx
                ic(mx)
                mn, min_index = min_heap[0]
                ic(mn)
                if mx-mn <= limit:

                    max_subarray_len = max(max_subarray_len, i-start+1)
                    break
                else:
                    start = min(max_index, min_index) + 1
                    ic(start)
                    while len(max_heap)>0 and max_heap[0][1] < start:
                        hq.heappop(max_heap)
                    while len(min_heap)>0 and min_heap[0][1] < start:
                        hq.heappop(min_heap)

        return max_subarray_len



c = Solution()
nums = [8,2,4,7]
ic(nums)
res = c.longestSubarray(nums,4)
ic(res)

nums = [4,2,2,2,4,4,2,2]

ic(nums)
res = c.longestSubarray(nums,0)
ic(res)

nums = [10,1,2,4,7,2]
limit = 5
ic(nums)
res = c.longestSubarray(nums,limit)
ic(res)
