class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.deq = deque(maxlen = self.size)

    def insertFront(self, value: int) -> bool:
        if len(self.deq) == self.size:
            return False
        self.deq.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.deq) == self.size:
            return False
        self.deq.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.deq) > 0:
            self.deq.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.deq) > 0:
            self.deq.pop()
            return True
        return False

    def getFront(self) -> int:
        return self.deq[0] if len(self.deq) > 0 else -1

    def getRear(self) -> int:
        return self.deq[-1] if len(self.deq) > 0 else -1

    def isEmpty(self) -> bool:
        return len(self.deq) == 0

    def isFull(self) -> bool:
        return len(self.deq) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
