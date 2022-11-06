class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        cur_max = float('-inf')
        while l < r:
            cur_area = (r-l) * min(height[l], height[r])
            cur_max = max(cur_max, cur_area)
            
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return cur_max
