from icecream import ic

class Solution:
    def climbStairs(self, n: int) -> int:
        fib=[1,2]
        if n==1 or n==2:
            return fib[n-1]
        for i in range(2,n):
            fib_next=fib[0]+fib[1]
            fib[0]=fib[1]
            fib[1]=fib_next
            print(fib[1])

        return fib[1]

c = Solution()
n = 6
res = c.climbStairs(n)
ic(n)
ic(res)
