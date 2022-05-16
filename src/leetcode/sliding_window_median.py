import heapq as hq
from icecream import ic


class Solution:
    def medianSlidingWindow(self, nums: list, k: int) -> list:
        medians = []
        left_heap = []
        right_heap = []
        which_heap = {}
        for i in range(k):
            left_heap.append((-1*nums[i],i))
            which_heap[i]=0
        hq.heapify(left_heap)
        hq.heapify(right_heap)

        for i in range(k//2):
            elem = hq.heappop(left_heap)
            hq.heappush(right_heap, (-1*elem[0], elem[1]))
            which_heap[elem[1]] = 1

        for i in range(len(nums)-k+1):
            # ic(left_heap)
            # ic(right_heap)
            if k%2 == 1:
                med = 0
                for j in range(len(left_heap)):
                    elem = hq.heappop(left_heap)
                    if elem[1] >= i:
                        med = -1*elem[0]
                        hq.heappush(left_heap,elem)
                        break
                medians.append(med)
            else:
                med = 0
                for j in range(len(left_heap)):
                    elem = hq.heappop(left_heap)
                    if elem[1] >= i:
                        med = -1 * elem[0]
                        hq.heappush(left_heap,elem)
                        break
                for j in range(len(right_heap)):
                    elem = hq.heappop(right_heap)
                    if elem[1] >= i:
                        med =  (med + elem[0])/2
                        hq.heappush(right_heap,elem)
                        break
                medians.append(med)
            # ic(medians)

            if i+k < len(nums):
                # ic(nums[i+k],med)
                if nums[i+k] < med:
                    hq.heappush(left_heap, (-1*nums[i+k], i+k))
                    which_heap[i+k] = 0
                    if which_heap[i] == 1:
                        for j in range(len(left_heap)):
                            elem = hq.heappop(left_heap)
                            if elem[1] > i:
                                hq.heappush(right_heap, (-1 * elem[0], elem[1]))
                                which_heap[elem[1]] = 1
                                break

                else:
                    hq.heappush(right_heap, (nums[i + k], i + k))
                    which_heap[i + k] = 1
                    if which_heap[i] == 0:
                        for j in range(len(right_heap)):
                            elem = hq.heappop(right_heap)
                            if elem[1] > i:
                                hq.heappush(left_heap, (-1 * elem[0], elem[1]))
                                which_heap[elem[1]] = 0
                                break
            # ic(window)

        return medians

c = Solution()
nums = [7,8,8,3,8,1,5,3,5,4]
k=3
ic(nums)
res = c.medianSlidingWindow(nums,k)
ic(res)

ic([1,3,-1,-3,5,3,6,7])
res = c.medianSlidingWindow([1,3,-1,-3,5,3,6,7],3)
ic(res)
nums = [1,2,3,4,2,3,1,4,2]
k = 3
ic(nums)
res = c.medianSlidingWindow(nums,k)
ic(res)
