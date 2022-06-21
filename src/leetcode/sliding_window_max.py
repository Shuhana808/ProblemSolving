



from collections import deque


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        res = []
        for i in range(0, len(nums)):

            while len(dq) != 0 and dq[-1][0] < nums[i]:
                dq.pop()

            dq.append((nums[i], i))

            if i >= k - 1:
                cw_max, ind = dq[0]

                if ind < i - k + 1:
                    dq.popleft()

                cw_max, ind = dq[0]
                res.append(cw_max)

        return res





