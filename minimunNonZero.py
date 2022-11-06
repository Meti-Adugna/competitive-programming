class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        x = (1<<p) - 1
        y = x - 1
        r = x
        mod = 1000000007
        for _ in range(p-1):
            r = r * y % mod
            y = y*y % mod
    
        return r
