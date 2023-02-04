class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        maxI = 0

        water = 0

        jumps = []

        for i in range(len(height)):
            #print("max", height[maxI])
            for j in range(i-1, maxI, -1):
                #print(height)
                #print(i,j)
                if height[i] <= height[j]:
                    break
                #print("check")
                #if height[i] >= height[j - 1] and height[j - 1] > height[i-1]:
                if height[j - 1] > height[i-1]:
                    topheight = min(height[i], height[j - 1])
                    baseheight = height[i -1]

                    waterheight = topheight - baseheight
                    base = (i - j)
                    water += waterheight * base

                    height[i-1] = topheight
                    #print("top", waterheight, base)
                    #print("added water", waterheight * base, i, j-1)

            if height[i] >= height[maxI]:
                maxI = i

        return water
        """

        left = 0
        right = len(height) - 1

        water = 0
        
        leftmax = height[0]
        rightmax = height[right]

        while left < right:
            if height[left] < height[right]:
                leftmax = max(leftmax, height[left])
                wat = leftmax - height[left]
                if wat > 0:
                    water += wat
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                wat = rightmax - height[right]
                if wat > 0:
                    water += wat
                right -= 1
        
        return water
