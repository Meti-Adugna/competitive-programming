class Solution:
    def calculate(self, s: str) -> int:
        last = 0
        curr = 0
        result = 0
        prev = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                curr = curr * 10 + int(char)
            if char in ('+', '-', '*', '/') or i == len(s) - 1:
                if prev == '+':
                    result += last
                    last = curr
                elif prev == '-':
                    result += last
                    last = -curr
                elif prev == '*':
                    last = last * curr
                elif prev == '/':
                    last = int(last / curr)
                prev = char
                curr = 0
        result += last
        return result
