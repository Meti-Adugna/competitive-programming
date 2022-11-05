class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxFreq = 0
        max_count = 0
        dict = {}
        for i in tasks:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
            if dict[i] > maxFreq:
                maxFreq = dict[i]
                max_count = 1
            elif dict[i] == maxFreq:
                max_count += 1
        
        if len(dict) <= n+1:
            return (maxFreq-1) * (n+1) + max_count
        else:
            return max((maxFreq-1) * (n+1) + max_count, len(tasks))
