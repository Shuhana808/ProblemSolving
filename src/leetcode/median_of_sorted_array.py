from typing import List
from icecream import ic

class Solution:

    def findIthElem(self, nums1,nums2, median_ind):
        m = len(nums1)
        n = len(nums2)

        median_ind = (m + n) // 2
        i1 = i2 = 0
        j1 = m-1; j2 = n-1
        mid1=mid2=0
        while i1 <= j1 or i1 <=j1:

            # if i2 > j2:
            #     mid1 = (i1 + j1) // 2
            #     return nums1[mid1]

            mid1 = (i1 + j1) // 2
            mid2 = (i2 + j2) // 2
            ic(i1,j1,i2,j2)
            ic(mid1, mid2)
            elem_count = mid1 + mid2 + 1
            ic(elem_count, median_ind)
            if elem_count < median_ind:
                if nums1[mid1] >= nums2[mid2]:
                    i2 = mid2 + 1

                if nums1[mid1] < nums2[mid2]:
                    i1 = mid1 + 1

            elif elem_count > median_ind:
                if nums1[mid1] > nums2[mid2]:
                    j1 = mid1 - 1
                elif nums1[mid1] < nums2[mid2]:
                    j2 = mid2 - 1
                else:
                    j1 = mid1 - 1
                    j2 = mid2 - 1

            else:
                if nums1[mid1] > nums2[mid2]:
                    i2 = mid2+1
                else:
                    i1 = mid1+1

        return nums2[mid2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        if (m+n) % 2 == 1:
            return self.findIthElem(nums1, nums2, (m+n)//2)
        else:
            res = self.findIthElem(nums1, nums2, (m + n) // 2)
            ic(res)
            # return (self.findIthElem(nums1, nums2, (m+n)//2)+self.findIthElem(nums1, nums2, (m+n)//2-1))/2
            return res



c = Solution()
# res = c.findMedianSortedArrays([4,7,12,16,21,24,28],[6,7,9,10,17,19])
res = c.findMedianSortedArrays([4,7,12,13,21,24,28,29],[6,7,14,15,17,19])
print(res)