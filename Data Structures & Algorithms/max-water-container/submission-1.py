class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        res = (end - start) * min(heights[start],heights[end])
        while start != end:
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
            new_vol = (end - start) * min(heights[start],heights[end])
            if new_vol > res:
                res = new_vol

        return res


        