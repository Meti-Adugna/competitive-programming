class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        push_ptr=0
        pop_ptr=0
        while push_ptr<len(pushed) and pop_ptr<len(popped):
            if stack and stack[-1]==popped[pop_ptr]:
                pop_ptr+=1
                stack.pop()
            else:
                stack.append(pushed[push_ptr])
                push_ptr+=1
        while pop_ptr<len(popped) and popped[pop_ptr]==stack[-1]:
            stack.pop()
            pop_ptr+=1
        return pop_ptr==len(popped)
