class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while l < r:
            low_num = numbers[l]
            high_num = numbers[r]
            if (low_num + high_num == target):
                return [l+1, r+1]
            elif (low_num + high_num > target):
                r -= 1
            elif (low_num + high_num < target):
                l += 1

