class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        num = 0
        for i in nums:
            if i in repeat:
                if repeat[i] == 1:
                    num += 1
                else:
                    num += repeat[i]
                
                repeat[i] += 1
            else:
                repeat[i] = 1
        return num
