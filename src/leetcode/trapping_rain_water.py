from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        dq = deque([])
        blocks = 0
        max_height = 0
        trapped = 0
        for i in range(0, n):
            # print(dq)
            if len(dq) == 0:
                dq.append((height[i], i))
                max_height = height[i]
                continue

            if height[i] >= max_height:
                left_height, left_ind = dq.popleft()
                blocks = 0

                while len(dq) > 0:
                    h, ind = dq.popleft()
                    blocks = blocks + h
                # print(left_height,left_ind,blocks)

                trapped = trapped + left_height * (i - left_ind - 1) - blocks
                # print(trapped)

                dq.append((height[i], i))
                max_height = height[i]


            else:
                dq.append((height[i], i))

        max_h = 0
        for i in range(len(dq) - 1, -1, -1):
            if i == len(dq) - 1:
                max_h, max_ind = dq[i]
                continue

            if dq[i][0] >= max_h:
                max_h, max_ind = dq[i]
                continue
            elif dq[i][0] < max_h:
                trapped = trapped + (max_h - dq[i][0])

        return trapped


