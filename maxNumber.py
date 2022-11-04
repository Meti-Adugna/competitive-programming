class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        ans = 0
        for key in d.keys():
            if key * 2 == k:
                ans += d[key] // 2
            elif d[k - key] > 0:
                mi = min(d[key], d[k - key])
                d[key] -= mi     
                d[k - key] -= mi
                ans += mi
        return ans
