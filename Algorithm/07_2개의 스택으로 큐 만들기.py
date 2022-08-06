class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        # stack2를 다시 stack1로 옮기기
        while self.stack2:
            v = self.stack2.pop()
            self.stack1.append(v)

        # stack1에 새로운 원소 push
        self.stack1.append(value)

        # 다시 stack1을 stack2로 옮기기
        while self.stack1:
            v = self.stack1.pop()
            self.stack2.append(v)

    def pop(self):
        return self.stack2.pop()


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print("pop ", queue.pop())
print("pop ", queue.pop())
print("pop ", queue.pop())
queue.push(4)
queue.push(5)
print("pop ", queue.pop())
print("pop ", queue.pop())
