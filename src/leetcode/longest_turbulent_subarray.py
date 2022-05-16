

class Solution:
    def maxTurbulenceSize(self, arr: list) -> int:
        comp = [0]*(len(arr)-1)
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                comp[i-1] = 1
            elif arr[i] < arr[i-1]:
                comp[i-1] = 0
            else:
                comp[i-1] = 2

        print(comp)
        start = end = 0

        if len(arr) > 0:
            max_len = 1
        else:
            max_len = 0

        for i in range(0, len(comp)):
            if (i<len(comp)-1) and ((comp[i] == 0 and comp[i+1] == 1) or (comp[i] == 1 and comp[i+1] == 0)):
                end = i + 1
                current = (end - start) + 2
                max_len = max(max_len, current)

            elif comp[i]!=2:
                end = i
                current = (end - start) + 2
                max_len = max(max_len, current)
                start = i + 1

            else:
                start = i + 1

        return max_len


c = Solution()
res = c.maxTurbulenceSize([9,4,2,10,7,8,8,1,9])
print(res)

res = c.maxTurbulenceSize([0,1,1,0,1,0,1,1,0,0])
print(res)


res = c.maxTurbulenceSize([100,102])
print(res)





