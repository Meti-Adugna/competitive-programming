class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ")":
                r_s = ""
                while stack and stack[-1] != "(":
                    r_s += stack.pop()

                stack.pop()

                stack += list(r_s)
            else:
                stack.append(i)
        return "".join(stack)
