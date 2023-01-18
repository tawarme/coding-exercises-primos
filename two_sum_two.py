class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right = 0
        left = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            sum = numbers[left] + numbers[right]
            if sum > target:
                left -= 1
            else:
                right += 1

        return right + 1 , left + 1
