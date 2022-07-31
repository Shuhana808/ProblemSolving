from collections import deque


class Solution:
    def numberOfWays(self, corridor: str) -> int:

        dq = deque([])

        n = len(corridor)

        c = 0

        for i in range(n):

            if corridor[i] == 'S':
                c += 1

                dq.append(i)

        if c % 2 == 1 or c == 0:
            return 0

        res = 1
        first = dq.popleft()
        second = dq.popleft()
        m = 1000000007

        while len(dq) > 0:
            first = dq.popleft()

            res = (res * (first - second)) % m

            second = dq.popleft()

        return res







