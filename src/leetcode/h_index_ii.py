from typing import List
from icecream import ic

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        i=0; j=n-1
        h_index=0
        while i<=j:
            mid = (i+j)//2
            ic(i,j,mid)

            if citations[mid]>=n-mid:
                if mid==0 or citations[mid-1]<=n-mid:
                    h_index = n-mid
                j=mid-1
            elif citations[mid]<n-mid:
                i=mid+1
        ic(h_index)
        return h_index


c = Solution()
n = [0]
res = c.hIndex(n)
ic(n)
ic(res)


