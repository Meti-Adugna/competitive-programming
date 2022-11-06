class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        curr=0
        for i in range(n):
            l.append(i+1)
        while n>1:
            l.pop(((curr-1+k)%n))
            curr=(curr-1+k)%n
            n=n-1
        return l[0]
