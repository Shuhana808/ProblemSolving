import heapq
from typing import List

class Solution:

    def maxResult(self, nums: List[int], k: int) -> int:

        max_k_scores = [(-1 * nums[0], 0)]

        scores = [0] * len(nums)
        scores[0] = nums[0]

        heapq.heapify(max_k_scores)
        for i in range(1, len(nums)):

            ind = -1
            score = 0
            while ind < max(0, i - k):
                score, ind = heapq.heappop(max_k_scores)

            scores[i] = nums[i] + -1 * score

            heapq.heappush(max_k_scores, (score, ind))
            heapq.heappush(max_k_scores, (-1 * scores[i], i))

        return scores[-1]

