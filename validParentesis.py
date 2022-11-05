class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}','[':']'}
        arr = []
        for i in s:
            if i in d:  # 1
                arr.append(i)
            elif len(arr) == 0 or d[arr.pop()] != i:  # 2
                return False
        return len(arr) == 0 # 3
