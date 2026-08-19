class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_tracker = {}
        for val in nums:
            if val not in num_tracker:
                num_tracker[val] = 1
            else:
                return True
        return False