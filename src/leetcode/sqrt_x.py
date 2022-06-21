from icecream import ic

class Solution:
    def mySqrt(self, x: int) -> int:


        i=0;j=int(x)

        while j>=i:
            mid = int((i+j)/2)
            # ic(i,j,mid)
            square = mid*mid
            if square > x:
                j = mid-1
            elif square < x:
                i = mid+1
            elif square == x:
                return mid

        return j


c = Solution()
n = 3
res = c.mySqrt(n)
ic(n)
ic(res)
