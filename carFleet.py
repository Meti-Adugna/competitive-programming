class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = [(i,j) for i,j in zip(position,speed)]
        ans.sort(reverse = True)
        stack = []
        for pos,speed in ans:
            time = (target-pos)/speed
        
            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)
