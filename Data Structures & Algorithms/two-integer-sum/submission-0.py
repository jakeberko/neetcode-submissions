from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        val_dict = defaultdict(int)
        for val in nums:
            if val in val_dict:
                return [val_dict[val], i]
            difference = target - val
            val_dict[difference] = i
            i += 1

