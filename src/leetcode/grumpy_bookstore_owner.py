from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:

        min_sat_cus = [0]*len(customers)

        k = 0
        for i in range(len(customers)):
            min_sat_cus[i] = k + customers[i] * (1-grumpy[i])
            k = min_sat_cus[i]

        max_sat = k

        for i in range(len(customers) - X + 1):
            if i:
                max_sat = max(max_sat, min_sat_cus[i - 1] + sum(customers[i:i + X]) + min_sat_cus[len(customers)-1] - min_sat_cus[i+X-1])
            else:
                max_sat = max(max_sat, sum(customers[i:i + X]) + min_sat_cus[len(customers)-1] - min_sat_cus[i+X-1])


        return max_sat


c = Solution()
res = c.maxSatisfied([1], [0], 1)
res = c.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3)
print(res)
