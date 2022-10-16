def waterArea(heights):
    # Write your code here.
    n = len(heights)
    res = 0
    i = 0
    while i < n - 1:
        if heights[i] == 0:
            i = i + 1
            continue
        j = i + 1
        max_j = j
        #get the first index j right to current index i where height is greater than or equal to current height (height[i])
        while j < n and heights[j] < heights[i]:
            if heights[j] >= heights[max_j]:
                max_j = j

            res -= heights[j]
            j += 1

        #if there is no such height that is greater than or equal to current height to the right than take the max of all
        #the heights right to current height and start iterating from there again.
        if j >= n:
            for k in range(max_j, n):
                res += heights[k]
            j = max_j

        res += min(heights[j], heights[i]) * (j - i - 1)
        print(i, j, res)
        i = j

    return res



