from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(num) for num in nums]

        def compare(x, y):
            x_c = x + y
            y_c = y + x
            
            if x_c > y_c:
                return 1
            elif x_c == y_c:
                return 0
            else:
                return -1
            
        nums.sort(key=cmp_to_key(compare), reverse=True)

        res = "".join(nums)

        return "0" if res[0] == "0" else res
