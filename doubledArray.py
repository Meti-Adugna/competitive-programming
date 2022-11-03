class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        stack,result=deque([]),[]
        for i in changed:
            if stack and stack[0]*2==i:
                b=stack.popleft()
                result.append(b)
            else:
                stack.append(i)
        return result if not stack else []
