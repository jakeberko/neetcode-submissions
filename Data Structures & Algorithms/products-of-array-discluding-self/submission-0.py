class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zs = 0
        zi = -1
        val = 1
        for i, num in enumerate(nums):
            if num == 0:
                zs += 1
                zi = i
            else:
                val = val * num
        
        if zs >= 2:
            array = [0] * len(nums)
            return array
        elif zs == 1:
            array = [0] * len(nums)
            array[zi] = val
            return array
        else:
            array = [val] * len(nums)
            for i in range(len(nums)):
                array[i] = array[i] // nums[i]
            return array


        

        