class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height) - 1

        area = 0

        while i < j:

            x = j - i
            y = min(height[i], height[j])
            current_area = x * y
            print(current_area)
            if current_area > area:
                area = current_area

            if height[i] < height[j]:
                i = i + 1

            else:
                j = j - 1

        return area
