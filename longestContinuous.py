class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lL = 0
        l, r = 0, 0
        n = len(nums)
        
        d_q = deque()
        i_q = deque()

        while r < n:
            while d_q and nums[d_q[-1]] < nums[r]:
                d_q.pop()
            d_q.append(r)
            while i_q and nums[i_q[-1]] > nums[r]:
                i_q.pop()
            i_q.append(r)
            
            
            while nums[d_q[0]] - nums[i_q[0]] > limit:
                l += 1
                if i_q[0] < l: i_q.popleft()
                if d_q[0] < l: d_q.popleft()
            
            lL = max(r - l + 1, lL)
            
            r += 1

        return lL
