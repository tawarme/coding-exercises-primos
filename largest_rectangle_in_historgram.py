class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        heights += [0]

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else (i - 1 - stack[-1])
                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area
