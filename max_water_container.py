class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return max_area
