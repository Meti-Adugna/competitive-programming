class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k > 0 and len(stack) > 0 and int(stack[-1]) > int(i):
                stack.pop()
                k -= 1
            stack.append(i)
        
        while k > 0:
            stack.pop()
            k -= 1
        # print(stack)
        return "0" if len(stack) ==0 else str(int("".join(stack)))
